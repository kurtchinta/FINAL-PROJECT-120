import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message
from django.contrib.auth.models import User
from .middleware import EncryptionMiddleware

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']


        encrypted_message = EncryptionMiddleware.encrypt(message)

        await self.save_message(username, room, encrypted_message)
        # Broadcast the message to the group
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'message': encrypted_message,
                'username': username
            }
        )

    async def chat_message(self, event):
        encrypted_message = event['message']
        username = event['username']

        decrypted_message = EncryptionMiddleware.decrypt(encrypted_message)

        # Send the message to WebSocket clients
        await self.send(text_data=json.dumps({
            'message': decrypted_message,
            'username': username
        }))

    @sync_to_async
    def save_message(self, username, room, encrypted_message):
        user = User.objects.get(username=username)
    # Create the message using the user instance
        Message.objects.create(user=user, username=username, room=room, content=encrypted_message)
