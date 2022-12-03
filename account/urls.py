from . import views
from django.urls import path

urlpatterns = [
    path('host-login/', views.host_login,name='host_login'),
    # path('<str:group_name>/', views.index),
]
