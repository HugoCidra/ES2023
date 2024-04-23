import pytest
from django.test import RequestFactory
from api.REQ8.views import get_username
import json
from api.utils import tokens


"""
Test that the correct error is given when the request method is not GET for get_username.
"""


def test_get_username_invalid_method():
    request = RequestFactory().post('/get_username/')
    response = get_username(request)

    assert response["status"] == 400


"""
Test that the correct error is given when the request method is GET but errors out because the user is not authenticated for get_username.
"""


def test_get_username_invalid_token():
    request = RequestFactory().get('/get_username/')
    response = get_username(request)
    content = json.loads(response.content)

    assert content['error']['code'] == 400
    assert content['error']['message'] == "invalid_token: User is not logged in"


"""
Test for a valid response from get_username with the correct method and valid token.
"""


@pytest.mark.django_db
def test_get_username_valid_token():
    # generate a valid token
    token = tokens.write_token({'id': 1}).decode('utf-8')

    header = {"HTTP_AUTHORIZATION": token}

    request = RequestFactory().get('/get_username/', **header)
    response = get_username(request)

    assert response.status_code == 200