import uuid

from django.conf import settings
from django.db import models


class Challenge(models.Model):
    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    id = models.CharField(primary_key=True, max_length=64, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=12, choices=DIFFICULTY_CHOICES, default="medium")
    time_limit = models.PositiveIntegerField(default=30)
    category = models.CharField(max_length=60, blank=True)
    target_html = models.TextField(blank=True)
    target_css = models.TextField(blank=True)
    target_js = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_suspended = models.BooleanField(default=False)
    available_from = models.DateTimeField(null=True, blank=True)
    available_until = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Submission(models.Model):
    TYPE_CHOICES = [
        ("test", "Test"),
        ("final", "Final"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name="submissions")
    html = models.TextField(blank=True)
    css = models.TextField(blank=True)
    js = models.TextField(blank=True)
    score_total = models.PositiveIntegerField(default=0)
    score_breakdown = models.JSONField(default=dict, blank=True)
    submission_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="test")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.challenge} ({self.submission_type})"


class LeaderboardEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name="leaderboard_entries")
    submission = models.ForeignKey(
        Submission,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leaderboard_entries",
    )
    score_total = models.PositiveIntegerField(default=0)
    score_breakdown = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-score_total", "-created_at"]

    def __str__(self) -> str:
        return f"{self.user} - {self.challenge} ({self.score_total})"
