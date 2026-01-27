from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import SystemState

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
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
            "updated_at",
        )
        read_only_fields = (
            "updated_at",
        )
