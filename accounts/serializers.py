from django.contrib.auth import get_user_model
from rest_framework import serializers

from django.utils import timezone

from .models import SystemSchedule, SystemState

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "public_id",
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "school",
        )




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class SystemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemState
        fields = (
            "allow_competitor_access",
            "scheduled_pause_active",
            "updated_at",
        )
        read_only_fields = (
            "scheduled_pause_active",
            "updated_at",
        )


class SystemScheduleSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = SystemSchedule
        fields = (
            "id",
            "name",
            "close_at",
            "open_at",
            "enabled",
            "status",
            "created_at",
            "updated_at",
        )

    def get_status(self, obj):
        now = timezone.now()
        if not obj.enabled:
            return "disabled"
        if obj.open_at <= now < obj.close_at:
            return "active"
        if obj.open_at > now:
            return "upcoming"
        return "completed"

    def validate(self, data):
        close_at = data.get("close_at")
        open_at = data.get("open_at")
        if self.instance is not None:
            if close_at is None:
                close_at = self.instance.close_at
            if open_at is None:
                open_at = self.instance.open_at
        if close_at and open_at and close_at <= open_at:
            raise serializers.ValidationError(
                {"close_at": "Close time must be after the open time."}
            )
        return data
