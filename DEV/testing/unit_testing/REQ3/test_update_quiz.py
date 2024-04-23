import json
import pytest
from django.test import RequestFactory
from jwt import decode
from api.models import Question, User, Tag, Option
from api.REQ3.views import update_quiz, new_quiz


@pytest.mark.django_db
def test_empty_payload():
    try:
        question = Question.objects.get(id=100)
        print(question)

        payload = {"body": "", "opt_text": "", "options": []}  # empty
        tag = "PM"
        state = 1  # urls.py

        update_quiz(payload, question, tag, state)
        quiz = Question.objects.filter(state=state).first()
        print(quiz)
        assert quiz is None

    except Question.DoesNotExist:
        print("Question not found.")
        AssertionError("Question not found.")


@pytest.mark.django_db
def test_verify_question_deletion():
    # new_quiz(
    #     {
    #         "tags": ["PM"],
    #         "body": "BODY_TEST1",
    #         "opt_text": "",
    #         "options": [
    #             {
    #                 id: 1,
    #                 "body": "OPTION1",
    #                 "is_correct": False,
    #                 "justification": "1",
    #             },
    #             {
    #                 id: 2,
    #                 "body": "OPTION2",
    #                 "is_correct": False,
    #                 "justification": "2",
    #             },
    #             {
    #                 id: 3,
    #                 "body": "OPTION3",
    #                 "is_correct": False,
    #                 "justification": "3",
    #             },
    #             {
    #                 id: 4,
    #                 "body": "OPTION4",
    #                 "is_correct": True,
    #                 "justification": "4",
    #             },
    #             {
    #                 id: 5,
    #                 "body": "OPTION5",
    #                 "is_correct": False,
    #                 "justification": "5",
    #             },
    #             {
    #                 id: 6,
    #                 "body": "OPTION6",
    #                 "is_correct": False,
    #                 "justification": "6",
    #             },
    #         ],
    #     },
    #     User.objects.get(id=1),
    #     4,
    # )

    update_quiz(
        {
            "tags": ["PM"],
            "body": "BODY_TEST1",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "OPTION1a",
                    "is_correct": False,
                    "justification": "1",
                },
                {
                    id: 2,
                    "body": "OPTION2a",
                    "is_correct": False,
                    "justification": "2",
                },
                {
                    id: 3,
                    "body": "OPTION3a",
                    "is_correct": False,
                    "justification": "3",
                },
                {
                    id: 4,
                    "body": "OPTION4a",
                    "is_correct": True,
                    "justification": "4",
                },
                {
                    id: 5,
                    "body": "OPTION5a",
                    "is_correct": False,
                    "justification": "5",
                },
                {
                    id: 6,
                    "body": "OPTION6a",
                    "is_correct": False,
                    "justification": "6",
                },
            ],
        },
        Question.objects.filter(body="BODY_TEST1")[0],
        ["PA"],
        4,
    )

    AssertionError(Option.objects.filter(body="OPTION1"))
    assert Option.objects.filter(body="OPTION1a")[0].body == "OPTION1a"
