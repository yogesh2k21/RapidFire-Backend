from django.shortcuts import render,redirect
from .models import Room,Chat,Quiz
import string
import random
from django.core.cache import cache

# Create your views here.

# ye view testing purpose ke liye h
def quiz_page(request,group_name):
    room, created = Room.objects.get_or_create(name=group_name)
    if created:
        print('New Group Created')
        # cache_group_name='user_count_'+group_name
        # cache.set(cache_group_name, 0,246060) # 24 hrs TTL (in seconds)
        quiz=Quiz.objects.create(host=request.user,room=room)
    else:
        print('Existing Group')
        # cache_group_name='user_count_'+group_name
        # cache.set(cache_group_name, 0,246060) # 24 hrs TTL (in seconds)
        print('user_count_'+str(cache.get('user_count_'+group_name)))
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
    cache_group_name='user_count_'+group_name
    cache.set(cache_group_name, 0,246060) # 24 hrs TTL (in seconds)

    # group = Group.objects.create(name=group_name)
    # print('New Group Created')
    # return render(request,'app/quiz_page.html',{'group_name':group_name})
    return redirect('quiz_page', group_name=group_name)

def home(request):
    # create room and join room wala page
    return render(request,'app/home.html')