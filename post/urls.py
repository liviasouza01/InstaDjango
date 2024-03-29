from django.urls import path
from post import views

app_name = 'post'
urlpatterns = [
    path('', views.feeds, name='home'),
    path('create-new-post/', views.create_post, name='create_post'),
    path('details/<uuid:id>', views.post_details, name='post_details'),
    path('search/', views.search, name='search'),
     # API
    path('post-comments/<uuid:pk>/comments/', views.PostViewSet.as_view({'get': 'comments'}), name='post_comments'),
]
