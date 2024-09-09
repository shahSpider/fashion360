from django.urls import path, include
from setup.views import homepage
from django.contrib.auth import views as auth_views
from rest_framework import routers
from setup.views import  UserRegister, UserLogin, UserLogout, UserView

# router = routers.DefaultRouter()
# router.register(r'register', UserRegister, 'register')
# router.register(r'login', UserLogin, 'login')
# router.register(r'logout', UserLogout, 'logout')
# router.register(r'userview', UserView, 'userview')

urlpatterns = [
    path("", homepage),
    path("api/register/", UserRegister.as_view(), name='user-register'),
    path("api/login/", UserLogin.as_view(), name="user-login"),
    path("api/logout/", UserLogout.as_view(), name="user-logout"),
    path("api/user/", UserView.as_view(), name="user-view")
]