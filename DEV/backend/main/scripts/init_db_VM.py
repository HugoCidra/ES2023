import bcrypt
import json
from api.utils import tokens
from django.test import RequestFactory
from api.models import *
from api.REQ3.views import new_quiz
from scripts.Quizzes import add_quizzes,quizzes
from api.REQ4.views import vote

def run():
    tags = [
        "ES",
        "AC",
        "BD",
        "COMP",
        "IPRP",
        "POO",
        "PPP",
        "RC",
        "SI",
        "SO",
        "TC",
        "TI",
    ]
    for tag in tags:
        new_tag = Tag(value=tag)
        new_tag.save()

    creators = [
        "James",
        "Mary",
        "David",
        "Jennifer",
        "Thomas",
        "Donald",
        "Sandra",
        "Brian",
        "Michelle",
        "Jeff",
        "Dorothy",
        "William",
        "Maria",
        "Joseph",
        "Nancy"]
    

    for creator in creators[:5]:
        CreateUser(creator, 2)

    for creator in creators[5:]:
        CreateUser(creator, 1)
        
    add_quizzes()

    

    """
    #aceitar 7 quizzes para cada user de 1 a 5 (total accepted=35)
    #como a partir do quizz 11 os quizzes foram criados de forma intercalada pelos users de 1 a 5  
    for j in range(35):
        accept_quiz(6,11+j)

    #cada user tem um quiz accepted(id: 0-10 quizz / 6-15 user)    
    for j in range(10):
        accept_quiz(1,j+1)    
    """
    

    


def CreateUser(username:str, userrole:int):
    new_password = bcrypt.hashpw("admin123".encode("u8"), bcrypt.gensalt())
    new_user = User(
        name=username,
        password=new_password.decode("u8"),
        email=username + "@email.com",
        role = userrole,
    )
    new_user.save()
    


        
