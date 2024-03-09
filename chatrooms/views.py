from django.shortcuts import render
from django.views import View


#When a user accesses the index page, this view responds by rendering the HTML content of the index.html template.
class Index(View):
	def get(self, request):
		return render(request, 'chatrooms/index.html')

#When a user accesses a specific room, this view responds by rendering the room.html template with the given room name.
class Room(View):
	def get(self, request, room_name):
		return render(request, 'room.html', {'room_name': room_name})

