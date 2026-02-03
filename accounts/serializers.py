from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from django.utils import timezone

from .models import RegistrationCode, SystemSchedule, SystemState
from .schools import SCHOOL_OPTIONS, normalize_school_name

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


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    invite_code = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "school",
            "invite_code",
        )

    def validate_invite_code(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Invitation code is required.")
        return value.strip().upper()

    def validate_school(self, value):
        normalized = normalize_school_name(value)
        if not normalized:
            raise serializers.ValidationError("Please select a school from the provided list.")
        return normalized

    def create(self, validated_data):
        validated_data.pop("invite_code", None)
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.role = "competitor"
        user.set_password(password)
        user.save()
        return user


class ProfileUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False, allow_blank=False, max_length=150)
    last_name = serializers.CharField(required=False, allow_blank=False, max_length=150)
    username = serializers.CharField(required=False, allow_blank=False, max_length=150)
    school = serializers.CharField(required=False, allow_blank=False, max_length=120)

    def validate_username(self, value):
        normalized = value.strip()
        user = self.context.get("user")
        exists = User.objects.filter(username__iexact=normalized)
        if user:
            exists = exists.exclude(pk=user.pk)
        if exists.exists():
            raise serializers.ValidationError("That username is already taken.")
        return normalized

    def validate_school(self, value):
        normalized = normalize_school_name(value)
        if not normalized:
            raise serializers.ValidationError("Please choose a school from the list.")
        return normalized


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField()
    new_password = serializers.CharField(min_length=8)
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        user = self.context.get("user")
        current_password = attrs.get("current_password")
        new_password = attrs.get("new_password")
        confirm_password = attrs.get("confirm_password")

        if not user or not user.check_password(current_password):
            raise serializers.ValidationError({"current_password": "Current password is incorrect."})

        if new_password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})

        validate_password(new_password, user=user)
        return attrs


class SchoolListSerializer(serializers.Serializer):
    schools = serializers.ListField(child=serializers.CharField())

    def to_representation(self, instance):
        return {"schools": SCHOOL_OPTIONS}


class RegistrationCodeSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    consumed_by_username = serializers.SerializerMethodField()

    class Meta:
        model = RegistrationCode
        fields = (
            "id",
            "code",
            "status",
            "is_active",
            "expires_at",
            "created_at",
            "consumed_at",
            "consumed_by_username",
        )

    def get_consumed_by_username(self, obj):
        return obj.consumed_by.username if obj.consumed_by else None


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
