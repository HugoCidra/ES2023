import json
from api.REQ3.views import get_quiz
from api.utils import tokens
from django.test import RequestFactory
import pytest

"""
testar a resposta da funcao quando o método do pedido está incorreto
"""
def test_get_quiz_invalid_method():
    request = RequestFactory().post('/get_quiz', data={})
    
    response = get_quiz(request, 1)
    content = json.loads(response.content)

    assert content['status'] == 404
    assert content['message'] == "wrong_request type"

"""
testa a resposta da funcao quando o token é inválido
"""
def test_get_quiz_invalid_token():
    invalid_token = "invalid_token"
    header = {"HTTP_AUTHORIZATION":invalid_token}

    request = RequestFactory().get('/is_solver', **header)
    response = get_quiz(request, 1)

    content = json.loads(response.content)
    assert content["error"]["code"] == 400

"""
testar utilizador inexistente
"""
@pytest.mark.django_db #para poder aceder à base de dados
def test_get_quiz_invalid_user():
    token = tokens.write_token({'id': 100}).decode('u8')
    header = {"HTTP_AUTHORIZATION":token}

    request = RequestFactory().get('/is_solver', **header)
    response = get_quiz(request, 1)

    content = json.loads(response.content)
    assert content["status"] == 404


"""
testar questao inexistente
"""
@pytest.mark.django_db #para poder aceder à base de dados
def test_is_solver_invalid_user():
    token = tokens.write_token({'id': 1}).decode('u8')
    header = {"HTTP_AUTHORIZATION":token}

    request = RequestFactory().get('/is_solver', **header)
    response = get_quiz(request, 123) #questao inexistente

    content = json.loads(response.content)
    assert content["status"] == 404
    assert content["message"] == "quiz not found or the quiz is owned by another user"


"""
testar questao nao editavel
"""
@pytest.mark.django_db
def test_get_quiz_question_not_editable():
    #inserir token valido associado a um utilizador existente
    token = tokens.write_token({'id': 1}).decode('u8')
    header = {"HTTP_AUTHORIZATION":token}

    request = RequestFactory().get('/is_solver', **header)
    response = get_quiz(request, 1)

    content = json.loads(response.content)
    assert content["code"] == 201

"""
testar com um utilizador válido e questao existente e válida
"""
@pytest.mark.django_db
def test_get_quiz_valido():
    #inserir token valido associado a um utilizador existente
    token = tokens.write_token({'id': 1}).decode('u8')
    header = {"HTTP_AUTHORIZATION":token}

    request = RequestFactory().get('/is_solver', **header)
    response = get_quiz(request, 5) #questao existente e do utilizador

    content = json.loads(response.content)
    assert content["success"] == "true"