from accounts.routing import websocket_urlpatterns as accounts_websocket_urlpatterns
from competition.routing import websocket_urlpatterns as competition_websocket_urlpatterns

__all__ = ["websocket_urlpatterns"]

websocket_urlpatterns = (accounts_websocket_urlpatterns + competition_websocket_urlpatterns)
