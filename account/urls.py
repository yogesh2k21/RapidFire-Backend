from . import views
from django.urls import path

urlpatterns = [
    path('host-login/', views.host_login,name='host_login'),
    path('logout_view/', views.logout_view,name='logout_view'),
    # path('<str:group_name>/', views.index),
]
