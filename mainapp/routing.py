from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r'ws/chat/<chat_id>/', consumers.ChatConsumer.as_asgi()),
]
