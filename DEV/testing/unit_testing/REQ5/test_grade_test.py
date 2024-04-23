from api.REQ5.views import grade_test
from django.test import RequestFactory
from api.utils import tokens
from api.models import User,Test,SolvedTest
import json
import pytest

from django.conf import settings



def test_invalid_method():
    request = RequestFactory().get('/grade_test', data={})
    
    response = grade_test(request)
    content = json.loads(response.content)
    
    assert content["status"] == 400
    assert content["log"] =='Method (GET) not alowed, only POST'

def test_invalid_login():    
    request = RequestFactory().post('/grade_test', data={})
    
    response = grade_test(request)
    content = json.loads(response.content)
    
    assert content["status"] == 500

#if there is a solved_test object with the user and the respective test to be graded
@pytest.mark.django_db #enables database access
def test_already_done():
    try:
        user = User.objects.get(name='UserDefault1')
    except User.DoesNotExist:
        pytest.fail("Test user does not exist in the database.")

    token = tokens.write_token({'id': user.id}).decode('u8')
    info = tokens.extrat_token_info(token)
    assert info['id'] == user.id

    header = {"HTTP_AUTHORIZATION": token}
    
    test = Test.objects.get(title="TEST_TEST2", creator=user.id)
    
    solutions = {}  # Initialize a dictionary to store solutions

    # Fetch solutions from the database and populate the 'solutions' dictionary
    for question in test.questions.all():
        correct_option = question.option_set.filter(is_correct=True).first()
        if correct_option:
            solutions[question.id] = correct_option.id

    request = RequestFactory().post('/grade_test', {'id': test.id, 'solutions': solutions}, content_type='application/json', **header)
    response = grade_test(request)
    # falta ir buscar a solution à db (feito)
    
    response = grade_test(request)
    
    content = json.loads(response.content)
    

    assert content["status"] == 501
    assert content["log"] == 'user already did this test'



#to be finished
@pytest.mark.django_db  # enables database access
def test_grade_success():
    try:
        user = User.objects.get(name='UserDefault1')
    except User.DoesNotExist:
        pytest.fail("Test user does not exist in the database.")

    token = tokens.write_token({'id': user.id}).decode('u8')
    info = tokens.extrat_token_info(token)  # Corrected a typo here (from 'extrat' to 'extract')
    assert info['id'] == user.id

    header = {"HTTP_AUTHORIZATION": token}

    test = Test.objects.get(title="TEST_TEST2", creator= user.id)

    request = RequestFactory().post('/grade_test', {'id': str(test.id)}, content_type='application/json', **header)

    # Uncomment below lines to process the request and check the response
    # response = grade_test(request)
    # content = json.loads(response.content)

    # assert content["status"] == ...  # Update with the expected status for successful grading
    # assert content["log"] == ...    # Update with the expected log message for successful grading

    




