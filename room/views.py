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
from pathlib import Path

        # Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from openpyxl import load_workbook
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
    # chats=Chat.objects.filter(room=room)
    quiz=Quiz.objects.get(room=room)
    print(quiz.questions.all())
    # questions=MCQ.objects.filter(room=room).values('problem_statement')
    questions=[]
    print(questions)
    return render(request,'app/manual_quiz_page.html',{'group_name':group_name,'questions':quiz.questions.all()})

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

def auto_quiz(request):
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
    return redirect('auto_quiz_page', group_name=group_name)

def auto_quiz_page(request,group_name):
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
    # chats=Chat.objects.filter(room=room)
    # quiz=Quiz.objects.get(room=room)
    # print(quiz.questions.all())

    # questions=MCQ.objects.filter(room=room).values('problem_statement')
    
    questions=get_excel_data(request)
    print(questions)
    return render(request,'app/auto_quiz_page.html',{'group_name':group_name,'questions':questions})

def get_excel_data(self):
    try:
        '''
        {
        question: Q,
        answers: [
            { "option": op1, "correct": cop1 },
            { "option": op2, "correct": cop2 },
            { "option": op3, "correct": cop3 },
            { "option": op4, "correct": cop4 },
        ]
        }
        '''
        Question=[]
        myfile=load_workbook(BASE_DIR/"static/quiz.xlsx")
        s=myfile['Sheet1']
        row=s.max_row
        column=s.max_column
        for r in range(2,row-1):
            # d={}
            # options=[]
            mcq=s.cell(row=r,column=1).value
            for c in range(1,5):
                # if c == 4:
                #     t={"option":s.cell(row=r,column=4).value,"correct":True}       
                # else:
                #     t={"option":s.cell(row=r,column=c).value,"correct":False}
                # options.append(t)
                ans=s.cell(row=r,column=4).value
            Question.append({"question":mcq,"answers":ans})       


        
            # op1=s.cell(row=r,column=1).value
            # op2=s.cell(row=r,column=2).value
            # op3=s.cell(row=r,column=3).value
            # op4=s.cell(row=r,column=4).value
            # t={
            #     "option":op1,
            #     "correct":False
            # }
        pass
    except Exception as e:
        print(e)
    return Question

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
    