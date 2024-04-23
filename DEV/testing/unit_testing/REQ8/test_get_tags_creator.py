from django.test import RequestFactory
import json
import pytest
from api.REQ8.views import get_tags_creator
from api.utils import tokens
from api.models import User, Question, Tag

def test_invalid_token():
    invalid_token = "invalid_token"
    header = {"HTTP_AUTHORIZATION": invalid_token}
    request = RequestFactory().get('/tags', **header)

    response = get_tags_creator(request)
    content = json.loads(response.content)

    assert content["error"]["code"] == 400
    assert content["error"]["message"] == 'invalid_token: User is not logged in'

@pytest.mark.django_db
def test_user_not_found():
    valid_token = tokens.write_token({'id': 999}).decode('u8')
    header = {"HTTP_AUTHORIZATION": valid_token}
    request = RequestFactory().get('/tags', **header)

    response = get_tags_creator(request)
    content = json.loads(response.content)

    assert content["status"] == 400
    assert content["response"] == 'could not find the user'

@pytest.mark.django_db
def test_tags_created_successfully():
    try:
        user1 = User.objects.get(name='UserDefault1')
    except (User.DoesNotExist, Tag.DoesNotExist):
        pytest.fail(f"Test user does not exist in the database")



    valid_token = tokens.write_token({'id': user1.id}).decode('u8')
    header = {"HTTP_AUTHORIZATION": valid_token}
    request = RequestFactory().get('/tags', **header)

    response = get_tags_creator(request)
    content = json.loads(response.content)

    assert content["status"] == 200