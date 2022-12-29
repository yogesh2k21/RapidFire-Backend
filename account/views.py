from rest_framework.decorators import api_view
import json
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth.models import BaseUserManager,AbstractUser,User
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout

# from .models import MyUser


# from rest_framework.authtoken.views import obtain_auth_token









# from django.http import JsonResponse
# # from rest_framework_simplejwt.views import TokenObtainPairView
# # from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework

# # Create your views here.
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['email'] = user.email
#         token['first_name'] = user.first_name
#         return token

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer

def host_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        print(request.POST['username'])
        print(request.POST['password'])
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # redirect('home')
            return HttpResponseRedirect(reverse('home'))
        else:
            # Return an 'invalid login' error message.
            print('user not exists')
            #message framework add krna h
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