# asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from line.consumers import CapacityConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myworld.settings')  # Replace 'myworld' if needed

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/capacity/", CapacityConsumer.as_asgi()),
        ])
    ),
})