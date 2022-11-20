from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/wsc/<str:group_name>/", consumers.CustomSyncConsumer.as_asgi()),
    path("ws/awsc/<str:group_name>/", consumers.CustomAsyncConsumer.as_asgi()),
]