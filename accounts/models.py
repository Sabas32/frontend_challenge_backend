import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("competitor", "Competitor"),
        ("viewer", "Viewer"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="competitor")
    school = models.CharField(max_length=120, blank=True)

    def __str__(self) -> str:
        return self.username


class SystemState(models.Model):
    allow_competitor_access = models.BooleanField(default=True)
    scheduled_pause_active = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "System State"

    @classmethod
    def current(cls):
        state, _ = cls.objects.get_or_create(pk=1)
        return state


class SystemSchedule(models.Model):
    name = models.CharField(max_length=120, blank=True)
    close_at = models.DateTimeField()
    open_at = models.DateTimeField()
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-close_at", "-open_at")

    def __str__(self) -> str:
        label = self.name or "Scheduled window"
        return f"{label} ({self.close_at} -> {self.open_at})"
