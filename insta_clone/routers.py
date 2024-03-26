#REST FRAMEWORK
from rest_framework.routers import SimpleRouter
from post.views import PostViewSet, CommentViewSet
from reaction.views import LikeViewSet
from user_profile.views import ProfileViewSet
from chatrooms.views import MessageViewSet

router = SimpleRouter()
router.register('create_post', PostViewSet)
router.register('likes', LikeViewSet)
router.register('comment', CommentViewSet)
router.register('user', ProfileViewSet)
router.register('chat', MessageViewSet)
