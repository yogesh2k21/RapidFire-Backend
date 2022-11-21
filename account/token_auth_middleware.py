from channels.db import database_sync_to_async
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser
from urllib.parse import parse_qs
from channels.auth import AuthMiddlewareStack

@database_sync_to_async
def get_user(scope):
    #to use JWT we have to just modify is get_user, we only have to find user
    try:
        x=scope
        print(x)
        token_key=parse_qs(scope['query_string'].decode("utf8"))["token"][0]
        print("chl gya code")
        token=Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()
    

class TokenAuthMiddleware:
    def __init__(self,inner):
        self.inner=inner

    def __call__(self,scope):
        return TokenAuthMiddlewareInstance(scope,self)


class TokenAuthMiddlewareInstance:
    def __init__(self,scope,middleware):
        self.middleware = middleware
        self.scope=dict(scope)
        self.inner=self.middleware.inner

    async def __call__(self,receive,send):
        # print('scope dekhle ',self.scope['query_string'].decode("utf8"))
        # self.scope['user']=await get_user(self.scope)
        self.scope['user'] = await get_user(self.scope)
        print('user fetched')
        return await self.inner(self.scope,receive,send)
        # inner=self.inner(self.scope)
        # return await inner(receive,send)
    
TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))