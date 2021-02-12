from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



import channels.layers
from asgiref.sync import async_to_sync
channel_layer = channels.layers.get_channel_layer()
def send_message(message):
    async_to_sync(channel_layer.group_send)(
        'event_sharif',
        {
            'type': 'send_message_to_frontend',
            'message': message
        }
    )




class TestView(APIView):
    def get(self, request):

        print('test')
        send_message('lalalalal')

        return Response({'data': 'ok'}, status=status.HTTP_200_OK)
    
