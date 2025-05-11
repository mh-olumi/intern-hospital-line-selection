from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from consumers import CapacityConsumer

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/capacity/', CapacityConsumer.as_asgi()),
    ]),
})
