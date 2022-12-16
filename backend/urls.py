from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from account.views import signup
# from rest_framewor import ( TokenRefreshView )
# from django.contrib.auth import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls")),  # new
    path("room/",include("room.urls")),
    path('get_token/', obtain_auth_token, name='get_token'),
    # path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/',signup,name='signup'),
]
