import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

import chatrooms.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "insta_clone.settings")
django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chatrooms.routing.websocket_urlpatterns
        )
    )
})
'''
application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(chatrooms.routing.websocket_urlpatterns))
        ),
    }
)
'''


