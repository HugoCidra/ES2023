from django.test import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from api.models import User  # Importa os modelos apropriados
from api.utils import tokens
from api.REQ7.views import send_info, load_info
import pytest
import json


def test_no_token():

    request = RequestFactory().get('/send_info')

    response = send_info(request)
    content = json.loads(response.content)

    assert content["status"] == 500
    assert content["log"] =='User not loged in'



def test_invalid_token():

    invalid_token = "invalid_token"
    header = {"HTTP_AUTHORIZATION":invalid_token}
    request = RequestFactory().post('/send_info', **header)

    response = load_info(request)
    content = json.loads(response.content)

    assert content["status"] == 500
    assert content["log"] =='Expired session'



@pytest.mark.django_db
def test_send_info():

    try:
        user = User.objects.get(name='UserDefault1')  # Retrieve user from the database
    except User.DoesNotExist:
        pytest.fail("Test user does not exist in the database.")

    token = tokens.write_token({'id': user.id}).decode('u8')
    header = {"HTTP_AUTHORIZATION": token}

    request = RequestFactory().get('/send_info/', **header)

    response = send_info(request)
    content = json.loads(response.content)


    assert content["status"] == 200


@pytest.mark.django_db
def test_send_info_invalid_method():
    request = RequestFactory().post('/send_info', data={})
    
    response = send_info(request)
    content = json.loads(response.content)
    
    assert content["status"] == 405
    assert content["log"] =='Method (POST) not alowed, only GET'



