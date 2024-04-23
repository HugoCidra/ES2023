import json
from api.REQ2.views import is_solver
from django.test import RequestFactory
from api.utils import tokens
import pytest

"""
testa a resposta da funcao quando o método do pedido está incorreto
"""
def test_is_solver_invalid_method():
    request = RequestFactory().put('/is_solver', data={})
    response = is_solver(request)

    assert response['status'] == 404

"""
testa a resposta da funcao quando o token é inválido
"""
def test_is_solver_invalid_token():
    invalid_token = "invalid_token"
    header = {"HTTP_AUTHORIZATION":invalid_token}

    request = RequestFactory().get('/is_solver', **header)
    response = is_solver(request)

    content = json.loads(response.content)
    assert content["error"]["code"] == 400

"""
testar utilizador inexistente
"""
@pytest.mark.django_db #para poder aceder à base de dados
def test_is_solver_invalid_user():
    token = tokens.write_token({'id': 100}).decode('u8')
    header = {"HTTP_AUTHORIZATION":token}

    request = RequestFactory().get('/is_solver', **header)
    response = is_solver(request)

    content = json.loads(response.content)
    assert content["status"] == 400

"""
testar com um utilizador válido
"""
@pytest.mark.django_db
def test_is_solver_valid_user():
    token = tokens.write_token({'id': 1}).decode('u8')
    header = {"HTTP_AUTHORIZATION":token}

    request = RequestFactory().get('/is_solver', **header)
    response = is_solver(request)

    content = json.loads(response.content)

    assert content["status"] == 200
    assert content['response'] == False #assert de acordoc om dados teste na base de dados