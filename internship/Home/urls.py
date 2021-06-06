from django.urls import path
from .views import hello,home

urlpatterns = [
    path('',hello),
    path('home/',home),
]