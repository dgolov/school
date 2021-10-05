from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime

from .models import Profile, Dialog

import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        async_to_sync(self.channel_layer.group_add)(
            str(self.chat_id),
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chat_id,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        text = text_data_json['text']
        from_user = text_data_json['from_user']

        async_to_sync(self.channel_layer.group_send)(
            self.chat_id,
            {
                'type': 'chat_message',
                'text': text,
                'from_user': from_user
            }
        )

    def chat_message(self, event):
        text = event['text']
        from_user = event['from_user']

        # dialog = Dialog.objects.get(pk=int(self.chat_id))

        print()

        self.send(text_data=json.dumps({
            'event': "Send",
            'attachment': None,
            'date_and_time': datetime.now().isoformat(),
            'dialog': self.chat_id,
            'text': text,
            'from_user': from_user,
            'system_message': False,
            'is_read': False,
        }))
