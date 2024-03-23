from django.urls import path
from reaction import views

#REST FRAMEWORK
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('likes', views.LikeViewSet)
#router.register('comment', views.CommentViewSet)

#=====================
app_name = 'reaction'
urlpatterns = [
    path('<uuid:id>/likes/', views.likes, name='likes'),
]
