import pytest
from django.test import RequestFactory
from api.REQ2 import views
import json
from api.utils import tokens

"""
Testa que dá erro correto quando o método do request não é GET
"""
def test_creators_invalid_method():
    request = RequestFactory().post('/creators/')
    response = views.creators(request)
    assert response['status'] == 404

"""
Testa que dá erro correto quando é o método correto, mas não têm token de autenticação.
"""
def test_creators_no_token():
    factory = RequestFactory()
    request = factory.get('/creators/')
    response = views.creators(request)
    content = json.loads(response.content)
    assert content['error']['code'] == 400
    assert content['error']['message'] == 'could not extract token info.'

"""
Testa se dá uma resposta válida quando o método é o correto, e quando o token é aceitado
"""
@pytest.mark.django_db
def test_creators_valid_token_valid_request():
    #gerar token válido
    token = tokens.write_token({'id': 1}).decode('u8')

    header = {"HTTP_AUTHORIZATION":token}

    request = RequestFactory().get('/creators/', **header)
    response = views.creators(request)
    content = json.loads(response.content)

    assert content['status'] == 200
    assert content['creators'] == [['UserDefault2', 40], ['UserDefault1', 2]] #assert de acordo com dados teste da base de dados
