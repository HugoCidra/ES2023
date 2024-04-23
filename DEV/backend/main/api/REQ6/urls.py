from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("test/", views.create_test),
    path("tags/", views.tags)
]