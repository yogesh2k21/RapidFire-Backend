from rest_framework.decorators import api_view
import json
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth.models import BaseUserManager,AbstractUser,User
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout


def host_login(request):
    if request.POST:
        if request.POST['username']=='' or request.POST['password']=='': 
            print('Required Credentials are not given')
            return render(request,'login.html')
        username = request.POST['username']
        password = request.POST['password']
        print('username ',request.POST['username'])
        print('password ',request.POST['password'])
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print('redirecting to home page')
            return HttpResponseRedirect(reverse('home'))
        else:
            print('user not exists')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


# signup ka bhi page bnega
# @api_view(['POST'])
def signup(request):
    # print(request.body)
    received_json_data = json.loads(request.body.decode("utf-8"))
    print(received_json_data['password'])
    try:
        user=User(
        first_name=received_json_data['first_name'],
        last_name=received_json_data['last_name'],
        email=received_json_data['email'],     
        username=received_json_data['email']        
        )
        user.set_password(received_json_data['password'])
        user.save()
    except Exception as e:
        print(e)
        return JsonResponse({"success":False,"message":"User with this Email already Exists!"})
    try:
        # c=Customer(user=user).save()
        pass
    except Exception as e:
        print(e)
    print(user)
    return JsonResponse({"success":True,"message":"Account Created successfully"})

def logout_view(request):
    logout(request)
    return redirect('host_login')
    # return HttpResponseRedirect(reverse('host_login'))