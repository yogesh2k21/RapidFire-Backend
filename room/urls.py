from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name="home"),
    path('quiz/', views.quiz,name="quiz"),

    path('join_room/', views.join_room,name="join_room"),
    path('<str:group_name>/', views.quiz_page,name="quiz_page"),
]
