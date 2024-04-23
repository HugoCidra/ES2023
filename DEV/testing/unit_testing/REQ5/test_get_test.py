from django.test import RequestFactory
from api.REQ5.views import get_test
import json
import pytest

from api.models import Test, User
from api.utils import tokens

PATH = '/api/REQ5/get_test/'

@pytest.mark.django_db
def test_get_test_passed():
    try:
        user = User.objects.get(name='UserDefault1')
    except User.DoesNotExist:
        pytest.fail("Test user does not exist in the database.")

    token = tokens.write_token({'id': user.id}).decode('u8')
    info=tokens.extrat_token_info(token)
    #assert info['id']==user.id
    header = {"HTTP_AUTHORIZATION":token} 

    test=Test.objects.get(title="TEST_TEST1", creator= user.id)

    # Create a request object using Django's RequestFactory
    request_factory = RequestFactory()
    request = request_factory.get(PATH, {'id':'1'},content_type='application/json',**header)  # Replace with the actual API endpoint URL


    # Call the view function and get the response
    response = get_test(request)

    # Parse the JSON response content
    content = json.loads(response.content)


    # Check the structure of the JSON response
    assert 'status' in content
    # Check the response status code
    assert content['status'] == 200


    assert 'questions' in content
    assert isinstance(content['questions'], list)
    
    
    for question in content['questions']:
        assert 'id' in question
        assert 'body' in question
        assert 'opts' in question
        assert isinstance(question['opts'], list)

        # Example assertions for the first option of the first question
        for option in question['opts']:
            assert 'id' in option
            assert 'body' in option

    # Add more assertions based on the specific response format of your API

    # Example assertion for checking the presence of the 'log' key in case of error
    if 'log' in content:
        assert 'Test not found' in content['log']

@pytest.mark.django_db
def test_get_test_not_found():
    try:
        user = User.objects.get(name='UserDefault1')
    except User.DoesNotExist:
        pytest.fail("Test user does not exist in the database.")
    token = tokens.write_token({'id': user.id}).decode('u8')
    info=tokens.extrat_token_info(token)
    assert info['id']==user.id
    header = {"HTTP_AUTHORIZATION":token} 

    # Create a request object using Django's RequestFactory
    request_factory = RequestFactory()
    request = request_factory.get(PATH, {'id':'10'},content_type='application/json',**header)  # Replace with the actual API endpoint URL


    # Call the view function and get the response
    response = get_test(request)

    # Parse the JSON response content
    content = json.loads(response.content)


    # Check the structure of the JSON response
    assert 'status' in content
    # Check the response status code
    assert content['status'] == 401

@pytest.mark.django_db
def test_get_test_wrong_method():
    
    request = RequestFactory().put(PATH, data={})
    
    response = get_test(request)
    content = json.loads(response.content)
    
    assert content["status"] == 400
"""
    # Create a request object using Django's RequestFactory
    request_factory = RequestFactory()
    request = request_factory.put(PATH, {'id':'1'})  # Replace with the actual API endpoint URL


    # Call the view function and get the response
    response = get_test(request)

    # Parse the JSON response content
    content = json.loads(response.content)


    # Check the structure of the JSON response
    assert 'status' in content
    # Check the response status code
    assert content['status'] == 400
    """

@pytest.mark.django_db
def test_get_test_invalid_login():
    request = RequestFactory().get(PATH, data={})
    
    response = get_test(request)
    content = json.loads(response.content)
    
    assert content["status"] == 500

