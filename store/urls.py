from django.contrib import admin
from django.urls import path,include
from store import views

urlpatterns = [
    path('', views.home, name='home')
]
