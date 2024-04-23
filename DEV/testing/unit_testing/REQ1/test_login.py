import pytest

import sys, os.path
app_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.append(app_dir)

from api.models import User
from api.REQ1 import views

from django.test import RequestFactory
import json


@pytest.mark.django_db
def test_login_successful():
    
    #login com credenciais corretas
    request = RequestFactory().put('/login', data={"username":"UserDefault1", "password":"admin123"}, content_type="application/json") #criar request
    response = views.login(request) 

    content = json.loads(response.content)
    assert content['status'] == 200  
    

@pytest.mark.django_db
def test_login_invalid_credentials():
  
    #fazer login com credenciais que não existem
    request = RequestFactory().put('/login', data={"username":"non_existent", "password":"non_existent"}, content_type="application/json") #criar request
    response = views.login(request)

    content = json.loads(response.content)
    assert content['status'] == 500
    assert content['log'] == "Invalid credentials"
    
    



def test_login_wrong_method():
    request = RequestFactory().get('/login', data={}) #criar request do tipo GET
    response = views.login(request) #correr request
    content = json.loads(response.content)
    assert content['status'] == 405
    assert content['log'] == "Method (GET) not alowed, only PUT"
   

def test_login_empty_body():
    request = RequestFactory().put('/login', data={}) #correr request sem dados
    response = views.login(request) #correr request
    content = json.loads(response.content)
    assert content['status'] == 500
    assert content['log'] == "empty / invalid body"