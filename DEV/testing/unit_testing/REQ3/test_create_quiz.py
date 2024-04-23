import json
import pytest
from api.REQ3.views import create_quiz
from api.utils import tokens
from django.test import RequestFactory
from jwt import decode

"""teste que dá o erro correto quando o método do request não é POST
"""


def test_wrong_method():
    request = RequestFactory().put("/create_quiz", data={})
    response = create_quiz(request, state=1)
    content = json.loads(response.content)
    assert content["status"] == 404


"""teste que dá o erro correto quando o token não é valido - user não está logged id
"""


def test_invalid_token():
    invalid_token = "invalid_token"
    header = {"HTTP_AUTHORIZATION": invalid_token}
    request = RequestFactory().post("/create_quiz", **header)
    response = create_quiz(request, state=1)

    content = json.loads(response.content)

    assert content["status"] == 400
    assert content["message"] == "could not extract token info."


"""teste que dá o erro correto quando o user id não é encontrado
"""


@pytest.mark.django_db
def test_user_not_found():
    token = tokens.write_token({"id": 100}).decode(
        "u8"
    )  # token de um utilizador que não existe
    header = {
        "HTTP_AUTHORIZATION": token
    }  # o token é passado no header do request campo authoriztion
    request = RequestFactory().post("/create_quiz", **header)
    response = create_quiz(request, state=1)
    content = json.loads(response.content)
    assert content["status"] == 400
    assert content["message"] == "User not found."


"""teste que dá o erro correto quando o não é passado um question_id
"""


@pytest.mark.django_db
def test_question_id_not_provided():
    token = tokens.write_token({"id": 1}).decode(
        "u8"
    )  # token de um utilizador que não existe
    header = {
        "HTTP_AUTHORIZATION": token
    }  # o token é passado no header do request campo authoriztion
    request = RequestFactory().post(
        "/create_quiz", data={}, content_type="application/json", **header
    )
    response = create_quiz(request, state=1)
    content = json.loads(response.content)
    assert content["status"] == 400
    assert content["message"] == "question_id not provided"


"""teste que dá o erro correto quando o question_id não é encontrado
"""


@pytest.mark.django_db
def test_question_not_found():
    token = tokens.write_token({"id": 1}).decode(
        "u8"
    )  # token de um utilizador que não existe
    header = {
        "HTTP_AUTHORIZATION": token
    }  # o token é passado no header do request campo authoriztion
    request = RequestFactory().post(
        "/create_quiz",
        data={"question_id": 100},
        content_type="application/json",
        **header
    )
    response = create_quiz(request, state=1)
    content = json.loads(response.content)
    assert content["status"] == 400
    assert content["message"] == "Quiz not found."


"""teste que verifica se está certo quando se cria uma questão nova
"""


@pytest.mark.django_db
def test_new_question_successful():
    token = tokens.write_token({"id": 1}).decode(
        "u8"
    )  # token de um utilizador que não existe
    header = {
        "HTTP_AUTHORIZATION": token
    }  # o token é passado no header do request campo authoriztion
    request = RequestFactory().post(
        "/create_quiz",
        data={
            "question_id": -1,
            "tags": ["PM"],
            "body": "",
            "opt_text": "",
            "options": [],
        },
        content_type="application/json",
        **header
    )
    response = create_quiz(request, state=1)
    content = json.loads(response.content)
    print(content["message"])
    assert content["status"] == 201


"""teste que verifica se está certo quando se atualiza uma questão 
"""


@pytest.mark.django_db
def test_update_question_successful():
    token = tokens.write_token({"id": 1}).decode(
        "u8"
    )  # token de um utilizador que não existe
    header = {
        "HTTP_AUTHORIZATION": token
    }  # o token é passado no header do request campo authoriztion
    request = RequestFactory().post(
        "/create_quiz",
        data={"question_id": 1, "tags": ["PM"], "body": "", "opt_text": "", "options": []},
        content_type="application/json",
        **header
    )
    response = create_quiz(request, state=1)
    content = json.loads(response.content)
    print(content["message"])
    assert content["status"] == 201
