'''

from django.urls import path
from .views import index, room

app_name='chatrooms'
urlpatterns = [
	path('', index.as_view(), name='index'),
	path('<str:room_name>/', room.as_view(), name='room'),
]
'''
from django.urls import path

from . import views
app_name = 'chatrooms'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]