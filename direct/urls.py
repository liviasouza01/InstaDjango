from direct.views import Inbox, Directs, SendDirect, UserSearch, NewConversation
from django.urls import path

urlpatterns = [
    path('', Inbox, name="message"),
    path('direct/<username>', Directs, name="directs"),
    path('send/', SendDirect, name="send-directs"),
    path('search/', UserSearch, name="search-users"),
    path('new/<username>', NewConversation, name="conversation"),
]