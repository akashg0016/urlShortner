from django.urls import path
from . import views
from homepage.views import index,routeToURL

urlpatterns = [
    path('',index),
    path('<slug:key>/',routeToURL)
]
