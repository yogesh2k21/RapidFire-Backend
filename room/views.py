from django.shortcuts import render,redirect
from .models import Room,Chat,Quiz,MCQ
from django.contrib.auth.models import User
import string
import random
from django.core.cache import cache
from django.http.response import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
#participant authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.utils.decorators import method_decorator
from .participant_middleware import get_user_middleware
from rest_framework.authtoken.models import Token
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
    quiz=Quiz.objects.get(room=room)
    print(quiz.questions.all())
    # questions=MCQ.objects.filter(room=room).values('problem_statement')
    questions=[]
    print(questions)
    return render(request,'app/quiz_page.html',{'group_name':group_name,'chats':chats,'questions':quiz.questions.all()})

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
    print('sdfdd',request.user.is_authenticated)
    # create room and join room wala page
    return render(request,'app/home.html')

#csrf is not given bcoz this is fetch api view
# @csrf_exempt
def join_room(request):
    json_data = json.loads(request.body.decode("utf-8"))
    try:
        quiz=Room.objects.filter(name=json_data["room_id"])[0]
        print(quiz)
        # return redirect('quiz_page', group_name=quiz.name)
        return JsonResponse(data={"exist":True},safe=False)
    except:
        print('room not exists')
        return JsonResponse(data={"exist":False},safe=False)
        
def fetch_user(request):
    json_data = json.loads(request.body.decode("utf-8"))
    # print(json_data,'json_data')

    key = request.headers['Authorization'].split(' ')[1]
    # print(key)
    response=None
    token=Token.objects.get(key=key)
    # print(token.user,'username')

    user=token.user
    group_name=json_data['group_name']
    # print(group_name,user)
    context={}
    context['user']=user
    context['body']=json_data
    return context

# @method_decorator(get_user_middleware)
@get_user_middleware
def submit_quiz_answers(request):
    # req=fetch_user(request)
    # print(req['user'])
    if request.method == 'POST':
        try:
            print(request.user.first_name)
            print(request.body)
            # json_data = json.loads(request.body.decode("utf-8"))
            # print('vews k ',request['user'])
            # u=request['user']
            # print(request.POST['group_name'])
            # print(request['group_name'],'<- group name')
            # json_data = request.headers['Authorization'].split(' ')[1]
            # print(json_data)
            return JsonResponse(data={'status':True,'message':'Successfully Submit'})
        except Exception as e:
            print(e)
            return JsonResponse(data={'status':False,'message':'Failed to submit'})
    else:
        return JsonResponse(data={'status':False,'message':'Failed to submit'})
    