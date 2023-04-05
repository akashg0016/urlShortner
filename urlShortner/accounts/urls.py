from django.urls import path
from .views import login,logout
from .views import register

urlpatterns = [
    
    path("",login, name="login"),
    path("register", register , name="register"),
    path("logout", logout,name="logout"),
]
