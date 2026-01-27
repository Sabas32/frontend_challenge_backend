from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
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
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "System State"

    @classmethod
    def current(cls):
        state, _ = cls.objects.get_or_create(pk=1)
        return state
