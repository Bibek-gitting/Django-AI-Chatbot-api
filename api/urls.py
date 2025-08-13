from django.urls import path
from .views import userRegister, userLogin, chat, userTokenBalance

urlpatterns = [
    path('register/', userRegister, name='user-register'),
    path('login/', userLogin, name='user-Login'),
    path('chat/', chat, name='chat'),
    path('usertokenbalance/', userTokenBalance, name='user-token-balance'),
]