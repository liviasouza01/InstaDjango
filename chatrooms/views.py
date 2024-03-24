from django.shortcuts import render
from .models import Message

from rest_framework import viewsets
from insta_clone.serializers import MessageSerializers


def index(request):
    return render(request, 'chatrooms/index.html')

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'room.html', {'room_name': room_name, 'username': username, 'messages': messages})

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers