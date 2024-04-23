import pytest
from django.test import RequestFactory
from api.REQ2 import views
import json
from api.utils import tokens

"""
Testa que dá erro correto quando o método do request não é GET
"""
def test_solvers_invalid_method():
    request = RequestFactory().post('/solvers/')
    response = views.solvers(request)
    assert response['status'] == 404

"""
Testa que dá erro correto quando é o método correto, mas não têm token de autenticação.
"""
def test_solvers_no_token():
    request = RequestFactory().get('/solvers/')
    response = views.solvers(request)
    content = json.loads(response.content)
    assert content['error']['code'] == 400
    assert content['error']['message'] == 'could not extract token info.'

"""
Testa se dá uma resposta válida quando o método é o correto, e quando o token é aceitado
"""
@pytest.mark.django_db
def test_solvers_valid_token_valid_request():
    #gerar token válido
    token = tokens.write_token({'id': 1}).decode('u8')

    header = {"HTTP_AUTHORIZATION":token}

    request = RequestFactory().get('/solvers/', **header)
    response = views.solvers(request)
    content = json.loads(response.content)

    assert content['status'] == 200
    assert content['solvers'] == [['UserSolver2', 0]] #assert de acordo com dados teste da base de dados
