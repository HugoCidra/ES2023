import json
from api.REQ2.views import unfinished_reproved_quizzes
from api.utils import tokens
from django.test import RequestFactory
import pytest


def test_register_invalid_method():
    request = RequestFactory().post("/unfinished_reproved", data={})
    response = unfinished_reproved_quizzes(request)
    assert response["status"] == 404


def test_invalid_token():
    invalid_token = "invalid_token"
    header = {"HTTP_AUTHORIZATION": invalid_token}
    request = RequestFactory().get("/unfinished_reproved", **header)
    response = unfinished_reproved_quizzes(request)

    content = json.loads(response.content)

    assert content["error"]["code"] == 400


@pytest.mark.django_db
def test_valid_token():
    token = tokens.write_token({"id": 1}).decode(
        "u8"
    )  # o token gerado é válido porque a função verify_token(tokens.py) apenas verifica se o token foi criado com o mesmo SECRET e não se o user é válido
    header = {
        "HTTP_AUTHORIZATION": token
    }  # o token é passado no header do request campo authorization
    request = RequestFactory().get("/unfinished_reproved", **header)
    response = unfinished_reproved_quizzes(request)

    content = json.loads(response.content)

    assert content["status"] == 200
    assert content["unfinished_reproved_quizzes"] == [
        [1, 4, "BODY_TEST1"],
        [2, 4, "BODY_TEST2"],
        [3, 2, "BODY_TEST3"],
        [4, 2, "BODY_TEST4"],
        [5, 3, "BODY_TEST5"],
    ]  # assert de acordo com dados teste da base de dados
