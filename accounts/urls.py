from django.urls import path

from .views import (
    CsrfView,
    LoginView,
    LogoutView,
    MeView,
    SystemScheduleDetailView,
    SystemScheduleListView,
    SystemStatusView,
    UserListView,
    OnlineUsersView,
)

urlpatterns = [
    path("csrf/", CsrfView.as_view(), name="csrf"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("me/", MeView.as_view(), name="me"),
    path("system-status/", SystemStatusView.as_view(), name="system-status"),
    path("users/", UserListView.as_view(), name="users"),
    path("online-users/", OnlineUsersView.as_view(), name="online-users"),
    path("system-schedules/", SystemScheduleListView.as_view(), name="system-schedules"),
    path(
        "system-schedules/<int:schedule_id>/",
        SystemScheduleDetailView.as_view(),
        name="system-schedule-detail",
    ),
]
