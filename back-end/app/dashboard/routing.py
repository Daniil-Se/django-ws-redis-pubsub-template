from channels.routing import URLRouter
from django.urls import path
from dashboard.consumer import Consumer


websockets = URLRouter([
    path(
    	"ws/params/",
    	Consumer.as_asgi(),
    	name='params'
    ),
])
