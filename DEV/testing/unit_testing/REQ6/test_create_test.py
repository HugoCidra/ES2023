from api.REQ6.views import create_test
from django.test import RequestFactory
from api.utils import tokens
from api.models import User, Question, Tag
import json
import pytest


# cd dev\backend
# .\venv\Scripts\activate
# pytest test_create_test.py


# CHECK FOR CORRECT METHOD IS NOT DONE IN create_test()

# def test_invalid_method():
#    request = RequestFactory().get('/test', data={})
#    response = create_test(request)


def test_invalid_token():
    invalid_token = "invalid_token"
    header = {"HTTP_AUTHORIZATION": invalid_token}
    request = RequestFactory().post("/test", **header)

    response = create_test(request)
    content = json.loads(response.content)

    assert content["status"] == 400
    assert content["errors"] == "invalid token"


# tags that dont have questions
@pytest.mark.django_db  # enables database access
def test_valid_token_emptytags():
    token = tokens.write_token({"id": 1}).decode("u8")
    header = {"HTTP_AUTHORIZATION": token}

    data = {"tags": ["<str>", "<str>"], "title": "<str>"}
    json_data = json.dumps(data)

    request = RequestFactory().post(
        "/test", json_data, content_type="application/json", **header
    )

    response = create_test(request)
    content = json.loads(response.content)

    assert content["status"] == 400
    assert content["errors"] == "Tag not found"


# tags with questions but dont add up to at least 20 (10 each tag)
@pytest.mark.django_db  # enables database access
def test_valid_token_not_enough_questions():
    try:
        user1 = User.objects.get(name="UserDefault1")  # Retrieve user from the database
    except User.DoesNotExist:
        pytest.fail("Test user does not exist in the database.")

    token = tokens.write_token({"id": user1.id}).decode(
        "u8"
    )  # change 'id':1 para user1.id
    header = {"HTTP_AUTHORIZATION": token}

    try:
        tag1 = Tag.objects.get(value="PM")  # see if tag is in the DB
        questions_for_tag1 = Question.objects.filter(tags=tag1)
        if not questions_for_tag1.exists():
            pytest.fail("No questions found for the given tag.")
        tag2 = Tag.objects.get(value="PA")
        questions_for_tag2 = Question.objects.filter(tags=tag2)
        if not questions_for_tag2.exists():
            pytest.fail("No questions found for the given tag.")
    except Tag.DoesNotExist:
        pytest.fail("Tag does not exist in the database.")

    data = {"tags": ["PM", "PA"], "title": "<str>"}

    json_data = json.dumps(data)
    request = RequestFactory().post(
        "/test", json_data, content_type="application/json", **header
    )

    response = create_test(request)
    response = create_test(request)
    response = create_test(request)
    content = json.loads(response.content)

    assert content["status"] == 400
    assert content["errors"] == "Not enough quizzes to make a test."


# valid token->tags with 20 questions(10 each) at least and test title ->success
@pytest.mark.django_db  # enables database access
def test_created_successfully():
    try:
        user1 = User.objects.get(name="UserDefault1")  # Retrieve user from the database
    except User.DoesNotExist:
        pytest.fail("Test user does not exist in the database.")

    token = tokens.write_token({"id": user1.id}).decode("u8")
    header = {"HTTP_AUTHORIZATION": token}

    try:
        tag1 = Tag.objects.get(value="PM")  # see if tag is in the DB
        questions_for_tag1 = Question.objects.filter(tags=tag1)
        if questions_for_tag1.count() < 10:
            pytest.fail("Not enough questions found for the given tag.")
    except Tag.DoesNotExist:
        pytest.fail("Tag does not exist in the database.")

    try:
        tag2 = Tag.objects.get(value="PA")  # see if tag is in the DB
        questions_for_tag2 = Question.objects.filter(tags=tag2)
        if questions_for_tag2.count() < 10:
            pytest.fail("Not enough questions found for the given tag.")
    except Tag.DoesNotExist:
        pytest.fail("Tag does not exist in the database.")

    data = {"tags": ["PM", "PA"], "title": "teste"}
    json_data = json.dumps(data)
    request = RequestFactory().post(
        "/test", json_data, content_type="application/json", **header
    )

    response = create_test(request)
    content = json.loads(response.content)

    assert content["status"] == 200
    assert content["message"] == "Test created successfully"
