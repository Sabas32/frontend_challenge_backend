from rest_framework import serializers

from .models import Challenge, LeaderboardEntry, Submission


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = (
            "id",
            "title",
            "description",
            "difficulty",
            "time_limit",
            "category",
            "target_html",
            "target_css",
            "target_js",
            "is_active",
            "is_suspended",
            "available_from",
            "available_until",
            "created_at",
            "updated_at",
        )


class SubmissionSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    challenge_title = serializers.CharField(source="challenge.title", read_only=True)

    class Meta:
        model = Submission
        fields = (
            "id",
            "user",
            "challenge",
            "challenge_title",
            "html",
            "css",
            "js",
            "score_total",
            "score_breakdown",
            "submission_type",
            "created_at",
        )
        read_only_fields = ("user",)

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "username": obj.user.username,
            "name": obj.user.get_full_name() or obj.user.username,
            "role": getattr(obj.user, "role", None),
            "school": getattr(obj.user, "school", None),
        }


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    challenge_title = serializers.CharField(source="challenge.title", read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = (
            "id",
            "user",
            "challenge",
            "challenge_title",
            "score_total",
            "score_breakdown",
            "created_at",
        )
        read_only_fields = ("user",)

    def get_user(self, obj):
        return {
            "id": obj.user.id,
            "username": obj.user.username,
            "name": obj.user.get_full_name() or obj.user.username,
            "role": getattr(obj.user, "role", None),
            "school": getattr(obj.user, "school", None),
        }
