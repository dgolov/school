from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer
from datetime import datetime

import json


class ChatConsumer(WebsocketConsumer):
    """ Отправка и прием сообщений в чатах через web сокеты
    """
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
        print(1)
        text_data_json = json.loads(text_data)
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


class ReadMessages(WebsocketConsumer):
    """ Отправка уведомлений о прочитанных сообщениях """
    def connect(self):
        self.chat = self.scope['url_route']['kwargs']['chat_id']
        async_to_sync(self.channel_layer.group_add)(
            str(self.chat),
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.chat,
            self.channel_name
        )

    def receive(self, text_data):
        print(2)
        text_data_json = json.loads(text_data)
        message_list = text_data_json['message_list']

        async_to_sync(self.channel_layer.group_send)(
            self.chat,
            {
                'id': 'read_message',
                'message_list': message_list
            }
        )

    def read_message(self, event):
        print(event)
        message_list = event['message_list']

        self.send(text_data=json.dumps({
            'event': "Send",
            'message_list': message_list
        }))
