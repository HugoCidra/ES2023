import bcrypt
import json
from api.utils import tokens
from django.test import RequestFactory
from api.models import *
from api.REQ3.views import new_quiz
from api.REQ6.views import create_test


def run():
    # user default 1
    new_password = bcrypt.hashpw("admin123".encode("u8"), bcrypt.gensalt())
    new_user = User(
        name="UserDefault1",
        password=new_password.decode("u8"),
        email="UserDefault1@gmail.com",
        role=1,
    )
    new_user.save()

    # user solver 2
    new_password = bcrypt.hashpw("admin123".encode("u8"), bcrypt.gensalt())
    new_user = User(
        name="UserSolver2",
        password=new_password.decode("u8"),
        email="UserSolver2@gmail.com",
        role=2,
    )
    new_user.save()

    # user default 3
    new_password = bcrypt.hashpw("admin123".encode("u8"), bcrypt.gensalt())
    new_user = User(
        name="UserDefault2",
        password=new_password.decode("u8"),
        email="UserDefault1@gmail.com",
        role=1,
    )
    new_user.save()

    # user default 4
    new_password = bcrypt.hashpw("admin123".encode("u8"), bcrypt.gensalt())
    new_user = User(
        name="UserDefault3",
        password=new_password.decode("u8"),
        email="UserDefault1@gmail.com",
        role=1,
    )
    new_user.save()

    tags = ["PM", "PA", "PB"]
    for tag in tags:
        new_tag = Tag(value=tag)
        new_tag.save()

    # quiz 1 - not editable (accepted)
    new_quiz(
        {
            "tags": ["PB"],
            "body": "BODY_TEST1",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "OPTION1",
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

    # quiz 2 - not editable (accepted)
    new_quiz(
        {
            "tags": ["PB"],
            "body": "BODY_TEST2",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "OPTION1",
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

    # quiz 3 - not editable (in_valuation)
    new_quiz(
        {
            "tags": ["PB"],
            "body": "BODY_TEST3",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "OPTION1",
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
        2,
    )

    # quiz 4 - not editable (in_valuation)
    new_quiz(
        {
            "tags": ["PB"],
            "body": "BODY_TEST4",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "OPTION1",
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
        2,
    )

    # quiz 5 - editable (rejected)
    new_quiz(
        {
            "tags": ["PB"],
            "body": "BODY_TEST5",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "OPTION1",
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
        3,
    )

    for i in range(3):  # 3 * accepted - q1
        v = Vote(
            user_id=2 + i, is_approved=True, justification=" ", question_id=1
        )  # user 2, 3 ,4
        v.save()

    for i in range(3):  # 3 * accepted - q2
        v = Vote(
            user_id=2 + i, is_approved=True, justification=" ", question_id=2
        )  # user 2, 3 ,4
        v.save()

    for i in range(2):  # 2 * accepted - q3
        v = Vote(
            user_id=2 + i, is_approved=True, justification=" ", question_id=3
        )  # user 2, 3
        v.save()

    for i in range(2):  # 2 * rejected - q4
        v = Vote(
            user_id=2 + i, is_approved=False, justification=" ", question_id=4
        )  # user 2, 3
        v.save()

    # create 20 questions for a test
    for i in range(10):
        new_quiz(
            {
                "tags": ["PM"],
                "body": "TEST_QuizTestSolved" + str(i),
                "opt_text": "",
                "options": [
                    {
                        id: 1,
                        "body": "OPTION1",
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
            User.objects.get(id=3),
            4,
        )

    # create test
    for i in range(10):
        new_quiz(
            {
                "tags": ["PA"],
                "body": "TEST_QuizTestSolved" + str(i + 10),
                "opt_text": "",
                "options": [
                    {
                        id: 1,
                        "body": "OPTION1",
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
            User.objects.get(id=3),
            4,
        )

    # create test (creator = user1) solved by user 2
    token = tokens.write_token({"id": 1}).decode("u8")  # user_id = 1
    header = {"HTTP_AUTHORIZATION": token}
    data = {"tags": ["PM", "PA"], "title": "TEST_TEST1"}
    json_data = json.dumps(data)
    request = RequestFactory().post(
        "/test", json_data, content_type="application/json", **header
    )
    create_test(request)
    user_solver = User.objects.get(id=2)
    test_to_solve = Test.objects.get(id=1)
    new_solved_test = SolvedTest(user=user_solver, test=test_to_solve)
    new_solved_test.save()

    # create 20 questions for a test
    for i in range(10):
        new_quiz(
            {
                "tags": ["PM"],
                "body": "TEST_QuizTestNotSolved" + str(i),
                "opt_text": "",
                "options": [
                    {
                        id: 1,
                        "body": "OPTION1",
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
            User.objects.get(id=3),
            4,
        )

    # create test
    for i in range(10):
        new_quiz(
            {
                "tags": ["PA"],
                "body": "TEST_QuizTestNotSolved" + str(i + 10),
                "opt_text": "",
                "options": [
                    {
                        id: 1,
                        "body": "OPTION1",
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
            User.objects.get(id=3),
            4,
        )

    # create test by user 1
    token = tokens.write_token({"id": 1}).decode("u8")  # user_id = 1
    header = {"HTTP_AUTHORIZATION": token}
    data = {"tags": ["PM", "PA"], "title": "TEST_TEST2"}
    json_data = json.dumps(data)
    request = RequestFactory().post(
        "/test", json_data, content_type="application/json", **header
    )
    create_test(request)


"""

3 * user creator/default: -> id = 1, 3, 4
1 * user solver: -> id = 2

3 * tag: 
    PM -> id = 1
    PA -> id = 2
    PB -> id = 3


1 * quiz accepted: -> id = 1
    tag: "PB",
    body: "BODY_TEST1"
    (not editable)

1 * quiz accepted: -> id = 2
    tag: "PB",
    body: "BODY_TEST2"
    (not editable)    

1 * quiz in_evaluation: -> id = 3
    tag: "PB",
    body: "BODY_TEST3"
    (not editable)

1 * quiz in_evaluation: -> id = 4
    tag: "PB",
    body: "BODY_TEST4"
    (not editable)

1 * quiz rejected: -> id = 5
    tag: "PB",
    body: "BODY_TEST5"
    (editable)


3 * vote accepted -> q_id=1
3 * vote accepted -> q_id=2
2 * vote accepted -> q_id=3
2 * vote rejected -> q_id=4



1 * solved test: -> id = 1
    title - TEST_TEST1
    questions - TEST_QuizTestSolved
    creator - UserDefault1 -> id = 1
    solver - UserSolver2 -> id = 2
    20 questions - 10 PM, 10 PA -> created by id = 3

1 * test: -> id = 2
    title - TEST_TEST2
    questions - TEST_QuizTestSolved
    creator - UserDefault1 -> id = 1
    20 questions - 10 PM, 10 PA -> created by id = 3

first 5 quizzes created by user id1
next 40 quizzes (2tests) created by user id3
    
"""
