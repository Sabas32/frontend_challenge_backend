from datetime import timedelta
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True, blank=True)
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


class RegistrationCode(models.Model):
    code = models.CharField(max_length=16, unique=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_registration_codes",
    )
    expires_at = models.DateTimeField()
    consumed_at = models.DateTimeField(null=True, blank=True)
    consumed_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="consumed_registration_codes",
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.code} ({self.status})"

    @property
    def is_expired(self) -> bool:
        return timezone.now() >= self.expires_at

    @property
    def status(self) -> str:
        if not self.is_active:
            return "revoked"
        if self.consumed_at:
            return "used"
        if self.is_expired:
            return "expired"
        return "active"

    @classmethod
    def default_expiry(cls):
        return timezone.now() + timedelta(minutes=20)
