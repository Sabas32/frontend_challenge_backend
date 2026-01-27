from django.urls import path

from .views import CsrfView, LoginView, LogoutView, MeView, SystemStatusView

urlpatterns = [
    path("csrf/", CsrfView.as_view(), name="csrf"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("me/", MeView.as_view(), name="me"),
    path("system-status/", SystemStatusView.as_view(), name="system-status"),
]
