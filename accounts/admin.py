from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Profile", {"fields": ("role", "school")}),)
    list_display = ("username", "email", "role", "school", "is_staff")
    list_filter = ("role", "is_staff", "is_superuser")
