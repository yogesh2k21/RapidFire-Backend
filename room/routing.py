from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/wsc/room/<str:group_name>/", consumers.CustomSyncConsumer.as_asgi()),
    path("ws/awsc/room/<str:group_name>/", consumers.CustomAsyncConsumer.as_asgi()),
]