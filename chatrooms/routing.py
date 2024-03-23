

from django.urls import re_path
from .consumers import ChatConsumer
from . import consumers

websocket_urlpatterns = [
	re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi())
]
'''
#SUPOSTAMENTE CORRETO
websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]
'''