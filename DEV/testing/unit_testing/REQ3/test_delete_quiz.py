import json
from api.REQ3.views import delete_quiz
from django.test import RequestFactory
import pytest
from api.utils import tokens
from jwt import decode
from api.models import User, Question, Option

"""APAGAR ESTE IMPORT E UTILIZACAO QND TIVER CONFTEST.PY"""
from api.REQ3.views import new_quiz


"""testa que dá o erro correto quando o médtodo do request não é POST"""


def test_register_invalid_method():
    request = RequestFactory().put("/delete", data={})
    response = delete_quiz(request, 1)
    content = json.loads(response.content)
    assert content["status"] == 404


"""teste que dá o erro correto quando o token não é valido - user não está logged id"""


def test_invalid_token():
    invalid_token = "invalid_token"
    header = {"HTTP_AUTHORIZATION": invalid_token}
    request = RequestFactory().post("/delete", **header)
    response = delete_quiz(request, question_id=1)

    content = json.loads(response.content)

    assert content["error"]["code"] == 400
    assert content["error"]["message"] == "could not extract token info."


"""teste que dá o erro correto quando o question_id não é encontrado
"""


@pytest.mark.django_db
def test_question_id_not_valid():
    token = tokens.write_token({"id": -1}).decode(
        "u8"
    )  # token de um utilizador que não existe
    header = {
        "HTTP_AUTHORIZATION": token
    }  # o token é passado no header do request campo authorization
    request = RequestFactory().post("/delete", **header)
    response = delete_quiz(request, question_id=-1)
    content = json.loads(response.content)
    assert content["error"]["code"] == 404
    print(content["error"]["message"])


"""teste que verifica se está certo quando se elimina uma questão"""


@pytest.mark.django_db
def test_delete_question_successful():
    # new_quiz(
    #     {
    #         "tag": "PRC",
    #         "body": "BODY_TEST1",
    #         "opt_text": "",
    #         "options": [
    #             {
    #                 id: 1,
    #                 "body": "OPTION1",
    #                 "is_correct": False,
    #                 "justification": "1",
    #             },
    #             {
    #                 id: 2,
    #                 "body": "OPTION2",
    #                 "is_correct": False,
    #                 "justification": "2",
    #             },
    #             {
    #                 id: 3,
    #                 "body": "OPTION3",
    #                 "is_correct": False,
    #                 "justification": "3",
    #             },
    #             {
    #                 id: 4,
    #                 "body": "OPTION4",
    #                 "is_correct": True,
    #                 "justification": "4",
    #             },
    #             {
    #                 id: 5,
    #                 "body": "OPTION5",
    #                 "is_correct": False,
    #                 "justification": "5",
    #             },
    #             {
    #                 id: 6,
    #                 "body": "OPTION6",
    #                 "is_correct": False,
    #                 "justification": "6",
    #             },
    #         ],
    #     },
    #     User.objects.get(id=1),
    #     4,
    # )

    token = tokens.write_token({"id": 1}).decode(
        "u8"
    )  # token de um utilizador que não existe
    header = {
        "HTTP_AUTHORIZATION": token
    }  # o token é passado no header do request campo authoriztion
    request = RequestFactory().post("/delete", **header)
    response = delete_quiz(request, question_id=1)
    content = json.loads(response.content)

    assert content["success"] == "true"
    assert content["code"] == 200
    assert content["message"] == "Quiz deleted succesfully."


"""teste que verifica se está certo quando se elimina uma questão"""


@pytest.mark.django_db
def test_verify_question_deletion():
    # new_quiz(
    #     {
    #         "tag": "PRC",
    #         "body": "BODY_TEST1",
    #         "opt_text": "",
    #         "options": [
    #             {
    #                 id: 1,
    #                 "body": "OPTION1",
    #                 "is_correct": False,
    #                 "justification": "1",
    #             },
    #             {
    #                 id: 2,
    #                 "body": "OPTION2",
    #                 "is_correct": False,
    #                 "justification": "2",
    #             },
    #             {
    #                 id: 3,
    #                 "body": "OPTION3",
    #                 "is_correct": False,
    #                 "justification": "3",
    #             },
    #             {
    #                 id: 4,
    #                 "body": "OPTION4",
    #                 "is_correct": True,
    #                 "justification": "4",
    #             },
    #             {
    #                 id: 5,
    #                 "body": "OPTION5",
    #                 "is_correct": False,
    #                 "justification": "5",
    #             },
    #             {
    #                 id: 6,
    #                 "body": "OPTION6",
    #                 "is_correct": False,
    #                 "justification": "6",
    #             },
    #         ],
    #     },
    #     User.objects.get(id=1),
    #     4,
    # )

    token = tokens.write_token({"id": 1}).decode(
        "u8"
    )  # token de um utilizador que não existe
    header = {
        "HTTP_AUTHORIZATION": token
    }  # o token é passado no header do request campo authoriztion
    request = RequestFactory().post("/delete", **header)
    response = delete_quiz(request, question_id=1)
    content = json.loads(response.content)

    AssertionError(Option.objects.filter(body="OPTION1"))
    AssertionError(Question.objects.filter(body="BODY_TEST1"))
