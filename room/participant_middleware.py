from rest_framework.authtoken.models import Token
import json
from django.http.response import JsonResponse

def get_user_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        try:
            key = request.headers['Authorization'].split(' ')[1]
            token=Token.objects.get(key=key)
            user=token.user
            request.user=user
            print('user fetched from token in middleware')
            return get_response(request)
        except Exception as e:
            print(e)
            return JsonResponse(data={'status':False,'message':'You have done some Misconfiguration with your device, Login again!!'})
    return middleware