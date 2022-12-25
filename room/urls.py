from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name="home"),
    path('auto_quiz/', views.auto_quiz,name="auto_quiz"),
    path('aquiz/<str:group_name>/', views.auto_quiz_page,name="auto_quiz_page"),

    path('custom_quiz/', views.quiz,name="custom_quiz"),
    path('quiz/<str:group_name>/', views.quiz_page,name="quiz_page"),
    
    path('join_room/', views.join_room,name="join_room"),
    path('submit_quiz_answers/', views.submit_quiz_answers,name="submit_quiz_answers"),
]
