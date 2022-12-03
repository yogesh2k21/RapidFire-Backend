from django.shortcuts import render
from .models import Group,Chat

# Create your views here.
def index(request,group_name):
    group, created = Group.objects.get_or_create(name=group_name)
    if created:
        print('New Group Created')
    else:
        print('Existing Group')
    chats=Chat.objects.filter(group=group)
    return render(request,'app/index.html',{'group_name':group_name,'chats':chats})

def home(request):
    return render(request,'app/home.html')