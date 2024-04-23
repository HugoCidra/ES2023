import bcrypt
from api.models import *
from api.REQ3.views import new_quiz

# run with python manage.py runscript init_db

def run():
    #create user1
    #warning security
    new_password = bcrypt.hashpw("admin123".encode('u8'), bcrypt.gensalt())
    new_user = User(name="justAUser1", password=new_password.decode('u8'), email="david@gmail.com",role=2)
    new_user.save()

    #create user2
    #warning security
    new_password = bcrypt.hashpw("admin123".encode('u8'), bcrypt.gensalt())
    new_user = User(name="justAUser2", password=new_password.decode('u8'), email="david@gmail.com",role=2)
    new_user.save()

    #create user3 - Creator with quizzes aproved and reproved
    #warning security
    new_password = bcrypt.hashpw("admin123".encode('u8'), bcrypt.gensalt())
    new_user = User(name="justAUser3", password=new_password.decode('u8'), email="david@gmail.com",role=1)
    new_user.save()


    #create user4 - Creator with nothing
    #warning security
    new_password = bcrypt.hashpw("admin123".encode('u8'), bcrypt.gensalt())
    new_user = User(name="justAUser4", password=new_password.decode('u8'), email="david@gmail.com",role=1)
    new_user.save()


    #create tags
    tags=["ES", "AC", "BD", "COMP", "IPRP", "POO", "PPP", "RC", "SI", "SO", "TC", "TI"]
    for tag in tags:
         new_tag=Tag(value=tag)
         new_tag.save()
    
    #-------------------User 1---------------------------
    #User mais completo, 20 quizes aceites, pelo menos 1 rejeitado, 
    