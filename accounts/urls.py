from django.urls import path

from .views import (
    CsrfView,
    LoginView,
    RegistrationCodeDetailView,
    RegistrationCodeListView,
    RegisterView,
    LogoutView,
    MeView,
    SystemScheduleDetailView,
    SystemScheduleListView,
    SystemStatusView,
    UserListView,
)

urlpatterns = [
    path("csrf/", CsrfView.as_view(), name="csrf"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("registration-codes/", RegistrationCodeListView.as_view(), name="registration-codes"),
    path("registration-codes/<int:code_id>/", RegistrationCodeDetailView.as_view(), name="registration-code-detail"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("me/", MeView.as_view(), name="me"),
    path("system-status/", SystemStatusView.as_view(), name="system-status"),
    path("users/", UserListView.as_view(), name="users"),
    path("system-schedules/", SystemScheduleListView.as_view(), name="system-schedules"),
    path(
        "system-schedules/<int:schedule_id>/",
        SystemScheduleDetailView.as_view(),
        name="system-schedule-detail",
    ),
]
