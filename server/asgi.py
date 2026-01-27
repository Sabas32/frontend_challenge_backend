"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

# Initialize Django first so app registry is ready before importing anything
# that touches models (like websocket routing/consumers).
django_asgi_app = get_asgi_application()

# Import routing only after Django setup completes.
from server.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
})
