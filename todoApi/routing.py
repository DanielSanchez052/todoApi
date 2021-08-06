import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from api.to_do.consumers import ToDoConsumer
from django.core.asgi import get_asgi_application
from api.to_do.routing import websocket_urlpatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoApi.settings.local')

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "http": get_asgi_application(),
    'websocket':URLRouter(
        websocket_urlpatterns
    ),
})




