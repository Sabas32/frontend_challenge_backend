from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.sessions.models import Session
from django.middleware.csrf import get_token
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SystemSchedule, SystemState
from .serializers import (
    LoginSerializer,
    SystemScheduleSerializer,
    SystemStatusSerializer,
    UserSerializer,
)
from .services import apply_schedule_state, build_system_status_payload

User = get_user_model()


@method_decorator(ensure_csrf_cookie, name="dispatch")
class CsrfView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        # In cross-site deployments (Vercel -> Render), the frontend cannot
        # read cookies for the backend domain. Return the token explicitly.
        token = get_token(request)
        return Response({"detail": "CSRF cookie set", "csrfToken": token})


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        state = SystemState.current()
        schedule_context = apply_schedule_state(state)
        if schedule_context.get("paused_now"):
            self._logout_competitors()
            self._notify_system_status(state, schedule_context)
        user = authenticate(
            request,
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if not user:
            return Response(
                {"detail": "Invalid username or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        system = SystemState.current()
        if (
            user.role == "competitor"
            and not system.allow_competitor_access
        ):
            return Response(
                {"detail": "Competitor access is currently disabled."},
                status=status.HTTP_403_FORBIDDEN,
            )
        login(request, user)
        return Response({"user": UserSerializer(user).data})

    def _logout_competitors(self):
        for session in Session.objects.all():
            data = session.get_decoded()
            user_id = data.get("_auth_user_id")
            if not user_id:
                continue
            user = User.objects.filter(pk=user_id).first()
            if user and user.role == "competitor":
                session.delete()

    def _notify_system_status(self, state, schedule_context=None):
        channel_layer = get_channel_layer()
        if not channel_layer:
            return
        payload = build_system_status_payload(state, schedule_context)
        async_to_sync(channel_layer.group_send)(
            "system_status",
            {
                "type": "system_status_update",
                "payload": payload,
            },
        )


class SystemStatusView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        state = SystemState.current()
        schedule_context = apply_schedule_state(state)
        if schedule_context.get("paused_now"):
            self._logout_competitors()
        if schedule_context.get("changed"):
            self._notify_system_status(state, schedule_context)
        payload = build_system_status_payload(state, schedule_context)
        return Response(payload)

    def patch(self, request):
        if not request.user.is_authenticated or request.user.role != "admin":
            return Response(
                {"detail": "Admin access required."},
                status=status.HTTP_403_FORBIDDEN,
            )
        state = SystemState.current()
        previous = state.allow_competitor_access
        serializer = SystemStatusSerializer(
            state, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        updated = serializer.save()
        if "allow_competitor_access" in request.data:
            updated.scheduled_pause_active = False
            updated.save(update_fields=["scheduled_pause_active", "updated_at"])
        if previous and not updated.allow_competitor_access:
            self._logout_competitors()
        schedule_context = apply_schedule_state(updated)
        if schedule_context.get("paused_now"):
            self._logout_competitors()
        payload = build_system_status_payload(updated, schedule_context)
        self._notify_system_status(updated, schedule_context)
        return Response(payload)

    def _logout_competitors(self):
        for session in Session.objects.all():
            data = session.get_decoded()
            user_id = data.get("_auth_user_id")
            if not user_id:
                continue
            user = User.objects.filter(pk=user_id).first()
            if user and user.role == "competitor":
                session.delete()

    def _notify_system_status(self, state, schedule_context=None):
        channel_layer = get_channel_layer()
        if not channel_layer:
            return
        payload = build_system_status_payload(state, schedule_context)
        async_to_sync(channel_layer.group_send)(
            "system_status",
            {
                "type": "system_status_update",
                "payload": payload,
            },
        )


class SystemScheduleListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        schedules = SystemSchedule.objects.all()
        serializer = SystemScheduleSerializer(schedules, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated or request.user.role != "admin":
            return Response(
                {"detail": "Admin access required."},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = SystemScheduleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        schedule = serializer.save()

        state = SystemState.current()
        schedule_context = apply_schedule_state(state)
        if schedule_context.get("paused_now"):
            self._logout_competitors()
        self._notify_system_status(state, schedule_context)
        return Response(SystemScheduleSerializer(schedule).data, status=201)

    def _logout_competitors(self):
        for session in Session.objects.all():
            data = session.get_decoded()
            user_id = data.get("_auth_user_id")
            if not user_id:
                continue
            user = User.objects.filter(pk=user_id).first()
            if user and user.role == "competitor":
                session.delete()

    def _notify_system_status(self, state, schedule_context=None):
        channel_layer = get_channel_layer()
        if not channel_layer:
            return
        payload = build_system_status_payload(state, schedule_context)
        async_to_sync(channel_layer.group_send)(
            "system_status",
            {"type": "system_status_update", "payload": payload},
        )


class SystemScheduleDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def patch(self, request, schedule_id):
        if not request.user.is_authenticated or request.user.role != "admin":
            return Response(
                {"detail": "Admin access required."},
                status=status.HTTP_403_FORBIDDEN,
            )
        schedule = SystemSchedule.objects.filter(pk=schedule_id).first()
        if not schedule:
            return Response(
                {"detail": "Schedule not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = SystemScheduleSerializer(
            schedule, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        updated = serializer.save()

        state = SystemState.current()
        schedule_context = apply_schedule_state(state)
        if schedule_context.get("paused_now"):
            self._logout_competitors()
        self._notify_system_status(state, schedule_context)
        return Response(SystemScheduleSerializer(updated).data)

    def delete(self, request, schedule_id):
        if not request.user.is_authenticated or request.user.role != "admin":
            return Response(
                {"detail": "Admin access required."},
                status=status.HTTP_403_FORBIDDEN,
            )
        schedule = SystemSchedule.objects.filter(pk=schedule_id).first()
        if not schedule:
            return Response(
                {"detail": "Schedule not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        schedule.delete()

        state = SystemState.current()
        schedule_context = apply_schedule_state(state)
        if schedule_context.get("paused_now"):
            self._logout_competitors()
        self._notify_system_status(state, schedule_context)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _logout_competitors(self):
        for session in Session.objects.all():
            data = session.get_decoded()
            user_id = data.get("_auth_user_id")
            if not user_id:
                continue
            user = User.objects.filter(pk=user_id).first()
            if user and user.role == "competitor":
                session.delete()

    def _notify_system_status(self, state, schedule_context=None):
        channel_layer = get_channel_layer()
        if not channel_layer:
            return
        payload = build_system_status_payload(state, schedule_context)
        async_to_sync(channel_layer.group_send)(
            "system_status",
            {"type": "system_status_update", "payload": payload},
        )


class LogoutView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        logout(request)
        return Response({"detail": "Logged out"})


class MeView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        if not request.user or not request.user.is_authenticated:
            return Response({"user": None})
        return Response({"user": UserSerializer(request.user).data})
