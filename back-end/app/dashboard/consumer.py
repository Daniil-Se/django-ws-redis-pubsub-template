# ws
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
# utils
import json


class Consumer(WebsocketConsumer):
    # http_user = True

    def connect(self):
        self.room_name = 'event'
        self.room_group_name = self.room_name+"_sharif"

         # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name) 
        self.accept()
        # при первичном соединении отдать именно ему
        # последнюю инфу из базы
        # self.send(text_data=json.dumps({
        #     'message': 'lasdas'
        # }))


    def disconnect(self, code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name)

    def receive(self, text_data=None, bytes_data=None):
        """Receive message from WebSocket"""
        json_data = json.loads(text_data)
        message = json_data
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                "type": 'send_message_to_frontend',
                "message": message
            }
        )

    def send_message_to_frontend(self, event):
        # Receive message from room group
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
