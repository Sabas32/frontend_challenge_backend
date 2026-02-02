from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import RegistrationCode, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Profile", {"fields": ("role", "school")}),)
    list_display = ("username", "email", "role", "school", "is_staff")
    list_filter = ("role", "is_staff", "is_superuser")


@admin.register(RegistrationCode)
class RegistrationCodeAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "created_by",
        "created_at",
        "expires_at",
        "consumed_by",
        "consumed_at",
        "is_active",
    )
    search_fields = ("code", "created_by__username", "consumed_by__username")
    list_filter = ("is_active", "created_at", "expires_at")
