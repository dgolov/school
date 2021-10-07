from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<chat_id>/', consumers.ChatConsumer.as_asgi()),
    path('ws/read-message/<chat_id>/', consumers.ReadMessages.as_asgi()),
]
