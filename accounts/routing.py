from django.urls import re_path

from .consumers import SystemStatusConsumer, OnlineUsersConsumer


websocket_urlpatterns = [
    re_path(r"^ws/system-status/$", SystemStatusConsumer.as_asgi()),
    re_path(r"^ws/online-users/$", OnlineUsersConsumer.as_asgi()),
]
