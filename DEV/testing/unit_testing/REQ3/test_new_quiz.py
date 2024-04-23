import json
from api.REQ3.views import new_quiz
from django.test import RequestFactory
from jwt import decode
import pytest
from api.models import User, Question, Option, Tag, Vote
from django.http import JsonResponse


# @pytest.mark.django_db
# def test_empty_payload():
#     try:
#         user = User.objects.get(id=4)

#         payload = {"body": "Empty_payload"}  # empty/partial
#         state = 5  # urls.py

#         new_quiz(payload, user, state)
#         quiz = Question.objects.filter(body="Empty_payload").first()
#         assert quiz is None

#     except User.DoesNotExist:
#         print("User not found.")
#         AssertionError("User not found.")


@pytest.mark.django_db
def test_verify_question_creation():
    new_quiz(
        {
            "tags": ["PB"],
            "body": "BODY_Creation_Test",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "OPTION_Creation_1",
                    "is_correct": False,
                    "justification": "1",
                },
                {
                    id: 2,
                    "body": "OPTION2",
                    "is_correct": False,
                    "justification": "2",
                },
                {
                    id: 3,
                    "body": "OPTION3",
                    "is_correct": False,
                    "justification": "3",
                },
                {
                    id: 4,
                    "body": "OPTION4",
                    "is_correct": True,
                    "justification": "4",
                },
                {
                    id: 5,
                    "body": "OPTION5",
                    "is_correct": False,
                    "justification": "5",
                },
                {
                    id: 6,
                    "body": "OPTION6",
                    "is_correct": False,
                    "justification": "6",
                },
            ],
        },
        User.objects.get(id=1),
        4,
    )

    q = Question.objects.filter(body="BODY_Creation_Test")

    assert q[0].body == "BODY_Creation_Test"


@pytest.mark.django_db
def test_verify_option_creation():
    new_quiz(
        {
            "tags": ["PB"],
            "body": "BODY_Creation_Test",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "OPTION_Creation_1",
                    "is_correct": False,
                    "justification": "1",
                },
                {
                    id: 2,
                    "body": "OPTION2",
                    "is_correct": False,
                    "justification": "2",
                },
                {
                    id: 3,
                    "body": "OPTION3",
                    "is_correct": False,
                    "justification": "3",
                },
                {
                    id: 4,
                    "body": "OPTION4",
                    "is_correct": True,
                    "justification": "4",
                },
                {
                    id: 5,
                    "body": "OPTION5",
                    "is_correct": False,
                    "justification": "5",
                },
                {
                    id: 6,
                    "body": "OPTION6",
                    "is_correct": False,
                    "justification": "6",
                },
            ],
        },
        User.objects.get(id=1),
        4,
    )

    op = Option.objects.filter(body="OPTION_Creation_1")

    assert op[0].body == "OPTION_Creation_1"
