from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('choose-test/', views.list_test),   # testes para selecionar
    path('get_test/', views.get_test),  # info nessessaria para resolver
    path('grade_test/', views.grade_test)   # pontuacao e solucoes
]
