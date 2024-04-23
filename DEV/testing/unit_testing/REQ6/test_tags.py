from django.test import RequestFactory
import json
import pytest
from api.REQ6.views import tags
from api.utils import tokens
from api.models import Tag

def test_invalid_method():
    request = RequestFactory().post('/tags', data={})
    response = tags(request)

    assert response.status_code == 405

def test_invalid_token():
    invalid_token = "invalid_token"
    header = {"HTTP_AUTHORIZATION": invalid_token}
    request = RequestFactory().get('/tags', **header)

    response = tags(request)
    content = json.loads(response.content)

    assert content["status"] == 400
    assert content["errors"] == 'invalid token'

@pytest.mark.django_db
def test_tags_retrieved_successfully():
    valid_token = tokens.write_token({'id': 1}).decode('u8')
    header = {"HTTP_AUTHORIZATION": valid_token}
    request = RequestFactory().get('/tags', **header)

    response = tags(request)
    content = json.loads(response.content)

    assert content["status"] == 200
    assert set(content["tags"]) == set(['PM', 'PB', 'PA'])
