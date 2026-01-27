from django.contrib import admin

from .models import Challenge, LeaderboardEntry, Submission


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "difficulty", "time_limit", "is_active", "created_at")
    search_fields = ("title", "description", "category")
    list_filter = ("difficulty", "is_active")


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "challenge", "submission_type", "score_total", "created_at")
    list_filter = ("submission_type",)
    search_fields = ("user__username", "challenge__title")


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "challenge", "score_total", "created_at")
    search_fields = ("user__username", "challenge__title")
