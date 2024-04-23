import pytest
from django.test import RequestFactory
from api.REQ4 import views
import json
from api.utils import tokens

"""
Testa que dá erro correto quando o método do request não é GET
"""

def test_quiz_invalid_method():
    request = RequestFactory().post('/quiz/')
    response = views.quiz(request)

    assert response is None


"""
Testa que dá erro correto quando o método do request é GET mas dá erro porque não está autenticado
"""


def test_quiz_invalid_token():
    request = RequestFactory().get('/quiz/')
    response = views.quiz(request)
    content = json.loads(response.content)
    assert content['status'] == 400


"""
Testa a resposta dos quizzes com o método certo e token válido, mas sem json com o id do user
"""


@pytest.mark.django_db
def test_quiz_valid_token_no_json():
    # gerar token válido
    token = tokens.write_token({'id': 1}).decode('u8')

    header = {"HTTP_AUTHORIZATION": token}

    request = RequestFactory().get('/quiz/', **header)
    response = views.quiz(request)
    assert response.status_code == 200


"""
Testa a resposta dos quizzes com o método certo e token válido, mas com json com o id do user
"""


@pytest.mark.django_db
def test_quiz_valid_token_no_json():
    # gerar token válido
    token = tokens.write_token({'id': 1}).decode('u8')

    header = {"HTTP_AUTHORIZATION": token}

    request = RequestFactory().get('/quiz/', **header, data={"id": 1}, content_type="application/json")
    response = views.quiz(request)
    assert response.status_code == 200