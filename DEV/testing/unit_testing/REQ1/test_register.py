import json
from api.REQ1 import register
from django.test import RequestFactory
import pytest
from jwt import decode

"""testa que dá o erro correto quando o médtodo do request não é POST
"""
def test_register_invalid_method():
    request = RequestFactory().put('/register', data={})
    response = register(request)
    content = json.loads(response.content)
    assert content['status'] == 405
    
    
"""testa  que dá o erro correto quando o payload está vazio"""
def test_register_empty_payload():
    request = RequestFactory().post('/register', data={}, content_type="application/json")
    response = register(request)
    content = json.loads(response.content)
    assert content['status'] == 500

"""testa que dá o erro correto quando não é enviado username"""
def test_register_missing_username():
    request = RequestFactory().post('/register', data={"password":"","email":""}, content_type="application/json")
    response = register(request)
    content = json.loads(response.content)
    assert content['status'] == 400
    assert content['log'] == "Param(s) username not found"

"""testa que dá o erro correto quando não é enviada a password"""
def test_register_missing_password():
    request = RequestFactory().post('/register', data={"username":"","email":""}, content_type="application/json")
    response = register(request)
    content = json.loads(response.content)
    assert content['status'] == 400
    assert content['log'] == "Param(s) password not found"


"""testa que dá o erro correto quando falta mais do que um parâmetro"""
def test_register_missing_multiple_properties():
    request = RequestFactory().post('/register', data={"email":""}, content_type="application/json")
    response = register(request)
    content = json.loads(response.content)
    assert content['status'] == 400
    assert content['log'] == "Param(s) username, password not found"

"""testa que aceita quando o email está vazio"""
@pytest.mark.django_db
def test_register_missing_email():
    request = RequestFactory().post('/register', data={"password":"","username":""}, content_type="application/json")
    response = register(request)
    content = json.loads(response.content)
    assert content['status'] == 200
   
""" testa que dá o erro correto quando o username já existe na BD""" 
@pytest.mark.django_db
def test_register_duplicated_user():
    request = RequestFactory().post('/register', data={"password":"password","username":"UserDefault1"}, content_type="application/json")
    
    response = register(request)
    content = json.loads(response.content)
    assert content['status'] == 500

""" testa que dá tudo certo quando os parâmetros estão corretos"""
@pytest.mark.django_db
def test_register_ok():
    request = RequestFactory().post('/register', data={"password":"password","username":"username","email" : ""}, content_type="application/json")
    
    response = register(request)
    content = json.loads(response.content)
    assert content['status'] == 200
    assert content['token'] != None
    assert decode(content['token'], options={"verify_signature": False})['id'] == 5 #verifica que o id do user para que foi criado o token está correto. Apenas válido sem o seed inicial da BD (conftest.py) (ALTERAR?)
    