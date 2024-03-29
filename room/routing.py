from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/awsc/room/<str:group_name>/", consumers.CustomAsyncConsumer.as_asgi()),
    path("ws/awsc/room/autoquiz/<str:group_name>/", consumers.AutoAsyncConsumer.as_asgi()),
]