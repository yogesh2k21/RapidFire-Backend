from django.shortcuts import render,redirect
from .models import Room,Chat,Quiz
import string
import random

# Create your views here.

# ye view testing purpose ke liye h
def quiz_page(request,group_name):
    room, created = Room.objects.get_or_create(name=group_name)
    if created:
        print('New Group Created')
        quiz=Quiz.objects.create(host=request.user,room=room)
    else:
        print('Existing Group')
    chats=Chat.objects.filter(room=room)
    return render(request,'app/quiz_page.html',{'group_name':group_name,'chats':chats})

def quiz(request):
    group_name=None
    while True:
        group_name = ''.join(random.choices(string.ascii_uppercase+string.digits, k=6))
        group = Room.objects.filter(name=group_name).exists()
        if not group:
            break
    # group_name = ''.join(random.choices(string.ascii_uppercase+string.digits, k=6))
    # chats=Chat.objects.filter(group=group)

    # group = Group.objects.create(name=group_name)
    # print('New Group Created')
    # return render(request,'app/quiz_page.html',{'group_name':group_name})
    return redirect('quiz_page', group_name=group_name)

def home(request):
    # create room and join room wala page
    return render(request,'app/home.html')