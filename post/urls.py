from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_view, name='post_view'),
    path('postdetails/<id>/', views.get_single_post, name='postdetails'),
    path('comment/<id>/', views.comment, name='comment'),
]