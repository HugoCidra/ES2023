from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("quiz/", views.quiz),
    path("vote/", views.vote)
]