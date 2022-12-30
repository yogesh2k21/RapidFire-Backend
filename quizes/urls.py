from . import views
from django.urls import path

urlpatterns = [
    path('', views.quiz_dashboard,name="quiz_dashboard"),
    path('<int:id>', views.quiz_detail,name="quiz_detail"),
]
