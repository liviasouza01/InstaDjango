from django.urls import path
from reaction import views

app_name = 'reaction'
urlpatterns = [
    path('<uuid:id>/likes/', views.likes, name='likes'),
    # API
    #path('likes/<uuid:pk>/likes/', views.LikeViewSet.as_view({'get': 'likes'}), name='likes'),

]

