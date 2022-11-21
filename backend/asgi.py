from account.token_auth_middleware import TokenAuthMiddleware,TokenAuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import room.routing
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': TokenAuthMiddlewareStack(
            AuthMiddlewareStack(URLRouter(room.routing.websocket_urlpatterns))
        )
        # 'websocket': AuthMiddlewareStack(
        #         URLRouter(
        #             room.routing.websocket_urlpatterns
        #         )
        # )
    }
)
