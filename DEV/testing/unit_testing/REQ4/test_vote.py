import json
from api.REQ1.views import register
from api.REQ4.views import vote
from api.REQ3.views import new_quiz
from api.utils import tokens
from django.test import RequestFactory
from api.models import Vote, Question, User
import pytest
import bcrypt
from jwt import decode

def aux_create_quiz(id_user):
    new_quiz(
        {
            "tag": "PRC",
            "body": "BODY_TEST1",
            "opt_text": "",
            "options": [
                {id: 1,"body": "OPTION1","is_correct": False,"justification": "1",},
                {id: 2,"body": "OPTION2","is_correct": False,"justification": "2",},
                {id: 3,"body": "OPTION3","is_correct": False,"justification": "3",},
                {id: 4,"body": "OPTION4","is_correct": True,"justification": "4",},
                {id: 5,"body": "OPTION5","is_correct": False,"justification": "5",},
                {id: 6,"body": "OPTION6","is_correct": False,"justification": "6",},
            ],
        },
        User.objects.get(id = id_user),
        1,
    )
def aux_create_vote(id_user,approved,id_question):
    v = Vote(user_id = id_user, is_approved = approved, justification = " ", question_id = id_question)
    v.save()

#valida o caso em que nao existe token no header
def test_without_token():
    request = RequestFactory().post('/vote',data = {},content_type="application/json")
    response = vote(request)
    
    content = json.loads(response.content)
    
    assert content["status"] == 400

#valida o caso em que e passado um token invalido
def test_invalid_token():
    invalid_token = "invalid_token"
    header = {"HTTP_AUTHORIZATION":invalid_token}
    request = RequestFactory().post('/vote', **header, data = {}, content_type="application/json")
    response = vote(request)
    
    content = json.loads(response.content)
    assert content["status"] == 400
    assert content["errors"] == "invalid token"

@pytest.mark.django_db
def test_verify_vote_creation():
    user_id = 1
    quest_id = 1
    token = tokens.write_token({'id': user_id}).decode('u8')#o token gerado é válido porque a função verify_token(tokens.py) apenas verifica se o token foi criado com o mesmo SECRET e não se o user é válido
    header = {"HTTP_AUTHORIZATION":token} #o token é passado no header do request campo authorization
    #o corpo do request envia o id da question em que se esta a votar
    request = RequestFactory().post('/vote', data = {"id":1,"accepted":True,"value":""}, **header, content_type = "application/json")
    response =vote(request)
    content = json.loads(response.content)
    new_vote = Vote.objects.filter(user_id = user_id,question_id = quest_id)
    
    assert new_vote != None
    assert content["status"] == 200
    assert content["message"] == "vote has been saved"
    
    
@pytest.mark.django_db   
def test_approved_question():
    
    #chamar a funcao vote com o user 4 para a question 3 (do user 1)
    #a question3 passa a ter 3 votes accepted portanto deve passar para o state 4(accepted)
    # e o role do user 1 deve passar de 1(creator) para 2 (solver)
    token = tokens.write_token({'id': 4}).decode('u8')#o token gerado é válido porque a função verify_token(tokens.py) apenas verifica se o token foi criado com o mesmo SECRET e não se o user é válido
    header = {"HTTP_AUTHORIZATION":token} #o token é passado no header do request campo authorization
    request = RequestFactory().post('/vote', data = {"id":3,"accepted":True,"value":""}, **header, content_type = "application/json")
    response = vote(request)
    content = json.loads(response.content)
    
    #verificar se o status da q1 passou a accepted
    q = Question.objects.get(id = 3)
    assert q.state == 4
    print("VOTES")
    print(Question.objects.filter(user__id=1, state = 4).count())
    #verificar se o user1 passou a solver
    user1 = User.objects.filter(id = 1)
    print("USER")
    print(user1[0].role)
    assert user1[0].role == 2
    
    #verificar se a questao foi aprovada
    assert content["status"] == 200
    assert content["message"] == f"question {3} has been approved"
    


@pytest.mark.django_db   
def test_rejected_question():
    
    #extrair o id da nova question criada
    q = Question.objects.filter(user=1)
    q_id = q[3].id #e a quiz 4 da bd que vai ser rejeitada 

    #chamar a funcao vote com o user 4 para a question4 (do user 1)
    #a question passa a ter 3 votes rejected portanto o state da question deve passar para 3(rejected)
    token = tokens.write_token({'id': 4}).decode('u8')#o token gerado é válido porque a função verify_token(tokens.py) apenas verifica se o token foi criado com o mesmo SECRET e não se o user é válido
    header = {"HTTP_AUTHORIZATION":token} #o token é passado no header do request campo authorization
    #o corpo do request envia o id da question em que se esta a votar
    request = RequestFactory().post('/vote', data = {"id":q_id,"accepted":False,"value":""}, **header, content_type = "application/json")
    response = vote(request)
    content = json.loads(response.content)
    
    #verificar se o status da question passou a rejected
    q = Question.objects.get(id = q_id)
    assert q.state == 3
    
    #verificar se a questao foi reprovada
    assert content["status"] == 200
    assert content["message"] == f"question {q_id} has been rejected"
    
