from channels.routing import ProtocolTypeRouter
from dashboard.routing import websockets


channels_routing = ProtocolTypeRouter({
    "websocket": websockets
})
