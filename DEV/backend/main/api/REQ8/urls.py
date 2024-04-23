from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('get_username/', views.get_username),
   path('get_stats_solver/', views.get_stats_solver),
   path('get_tags_creator/', views.get_tags_creator)
]
