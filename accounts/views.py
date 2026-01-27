from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SystemState
from .serializers import LoginSerializer, UserSerializer, SystemStatusSerializer

User = get_user_model()


class CsrfView(APIView):
    permission_classes = [permissions.AllowAny]

    @ensure_csrf_cookie
    def get(self, request):
        return Response({"detail": "CSRF cookie set"})


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
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


class SystemStatusView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        state = SystemState.current()
        serializer = SystemStatusSerializer(state)
        return Response(serializer.data)

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
        if previous and not updated.allow_competitor_access:
            self._logout_competitors()
        self._notify_system_status(updated)
        return Response(serializer.data)

    def _logout_competitors(self):
        for session in Session.objects.all():
            data = session.get_decoded()
            user_id = data.get("_auth_user_id")
            if not user_id:
                continue
            user = User.objects.filter(pk=user_id).first()
            if user and user.role == "competitor":
                session.delete()

    def _notify_system_status(self, state):
        channel_layer = get_channel_layer()
        if not channel_layer:
            return
        payload = {"allow_competitor_access": state.allow_competitor_access}
        async_to_sync(channel_layer.group_send)(
            "system_status",
            {
                "type": "system_status_update",
                "payload": payload,
            },
        )


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"detail": "Logged out"})


class MeView(APIView):
    def get(self, request):
        return Response({"user": UserSerializer(request.user).data})
