from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("unfinished_reproved/", views.unfinished_reproved_quizzes),
    path("solvers/", views.solvers),
    path("creators/", views.creators),
    path("is_solver/", views.is_solver),
]