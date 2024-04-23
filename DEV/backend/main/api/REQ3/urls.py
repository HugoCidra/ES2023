from django.urls import path
from .views import get_quiz, create_quiz, delete_quiz

urlpatterns = [
    path("save-quiz", create_quiz, kwargs={'state': 1}),
    path("get-quiz/<question_id>", get_quiz),
    path('submit-quiz', create_quiz, kwargs={'state': 2}),
    path('delete/<question_id>', delete_quiz)
]