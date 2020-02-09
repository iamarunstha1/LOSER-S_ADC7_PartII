from django.urls import path  
from Login.views import register
from Login.views import login
from Login.views import logout
from Login.views import index




urlpatterns = [
    path('index/',index),
    path("register/",register, name="register"),
    path("login/",login, name="login"),
    path("index/logout/",logout, name="logout"),
    path("login/logout/",logout, name="logout")

]

