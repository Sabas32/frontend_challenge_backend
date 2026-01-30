from django.urls import re_path

from .consumers import SystemStatusConsumer


websocket_urlpatterns = [
    re_path(r"^ws/system-status/$", SystemStatusConsumer.as_asgi()),
]
