from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("load_info/", views.load_info),
    path("send_info/", views.send_info),
]