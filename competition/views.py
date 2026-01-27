from rest_framework import permissions, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from accounts.permissions import IsAdminRole
from django.utils import timezone
from .models import Challenge, LeaderboardEntry, Submission
from .serializers import (
    ChallengeSerializer,
    LeaderboardEntrySerializer,
    SubmissionSerializer,
)


class ChallengeViewSet(viewsets.ModelViewSet):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all().order_by("-created_at")

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAuthenticated(), IsAdminRole()]
        return [permissions.AllowAny()]


class SubmissionViewSet(viewsets.ModelViewSet):
    def _ensure_challenge_available(self, challenge):
        if not challenge:
            return
        if challenge.is_suspended:
            raise ValidationError({"detail": "This challenge is suspended."})
        now = timezone.now()
        if challenge.available_from and now < challenge.available_from:
            raise ValidationError({"detail": "This challenge is not yet available."})
        if challenge.available_until and now > challenge.available_until:
            raise ValidationError({"detail": "This challenge is no longer available."})

    serializer_class = SubmissionSerializer
    queryset = Submission.objects.select_related("user", "challenge").all()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        if self.action in ["create"]:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated(), IsAdminRole()]

    def get_queryset(self):
        queryset = super().get_queryset()
        challenge_id = self.request.query_params.get("challenge")
        submission_type = (
            self.request.query_params.get("type")
            or self.request.query_params.get("submission_type")
        )
        user_param = self.request.query_params.get("user")
        user = getattr(self.request, "user", None)
        is_authenticated = bool(user and user.is_authenticated)
        is_admin = getattr(user, "role", None) == "admin"

        if not is_authenticated:
            # Public access: only expose final submissions when explicitly asked.
            if submission_type == "final":
                queryset = queryset.filter(submission_type="final")
            else:
                return queryset.none()
        elif not is_admin:
            queryset = queryset.filter(user=user)

        if challenge_id:
            queryset = queryset.filter(challenge_id=challenge_id)

        if submission_type:
            queryset = queryset.filter(submission_type=submission_type)

        if user_param and is_admin:
            if user_param.isdigit():
                queryset = queryset.filter(user_id=user_param)
            else:
                queryset = queryset.filter(user__username=user_param)

        return queryset.order_by("-score_total", "-created_at")

    def perform_create(self, serializer):
        challenge = serializer.validated_data.get("challenge")
        self._ensure_challenge_available(challenge)
        submission = serializer.save(user=self.request.user)
        if submission.submission_type == "final":
            self._upsert_leaderboard_entry(submission)

    def _upsert_leaderboard_entry(self, submission):
        entry = (
            LeaderboardEntry.objects.filter(
                user=submission.user, challenge=submission.challenge
            )
            .order_by("-created_at")
            .first()
        )
        if entry:
            entry.score_total = submission.score_total
            entry.score_breakdown = submission.score_breakdown or {}
            entry.submission = submission
            entry.save(update_fields=["score_total", "score_breakdown", "submission"])
        else:
            LeaderboardEntry.objects.create(
                user=submission.user,
                challenge=submission.challenge,
                submission=submission,
                score_total=submission.score_total,
                score_breakdown=submission.score_breakdown or {},
            )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    serializer_class = LeaderboardEntrySerializer
    queryset = LeaderboardEntry.objects.select_related("user", "challenge").all()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsAdminRole()]

    def get_queryset(self):
        queryset = super().get_queryset()
        challenge_id = self.request.query_params.get("challenge")
        user_param = self.request.query_params.get("user")

        if challenge_id:
            queryset = queryset.filter(challenge_id=challenge_id)
        if user_param:
            if user_param.isdigit():
                queryset = queryset.filter(user_id=user_param)
            else:
                queryset = queryset.filter(user__username=user_param)

        return queryset.order_by("-score_total", "-created_at")
