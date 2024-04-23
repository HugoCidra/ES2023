from django.test import RequestFactory
from api.REQ5.views import list_test
import json
import pytest

from api.models import SolvedTest, Test, User
from api.utils import tokens

PATH = '/api/REQ5/choose-test/'

@pytest.mark.django_db
def test_list_test_passed():
    try:
        user = User.objects.get(name='UserDefault1')
    except User.DoesNotExist:
        pytest.fail("Test user does not exist in the database.")
    token = tokens.write_token({'id': user.id}).decode('u8')
    info=tokens.extrat_token_info(token)
    assert info['id']== user.id
    header = {"HTTP_AUTHORIZATION":token} 

    Test.objects.get(title="TEST_TEST1", creator=user.id)
    Test.objects.get(title="TEST_TEST2", creator=user.id)

    # Create a request object using Django's RequestFactory
    request_factory = RequestFactory()
    request = request_factory.get(PATH, {},content_type='application/json',**header) 


    # Call the view function and get the response
    response = list_test(request)

    # Parse the JSON response content
    content = json.loads(response.content)


    # Check the structure of the JSON response
    assert 'status' in content
    # Check the response status code
    assert content['status'] == 200


    assert 'tests' in content
    assert isinstance(content['tests'], list)
    
    
    for test in content['tests']:
        assert 'id' in test
        assert 'title' in test
        assert 'tags' in test
        assert isinstance(test['tags'], list)


    # Example assertion for checking the presence of the 'log' key in case of error
    if 'log' in content:
        assert 'Test not found' in content['log']


@pytest.mark.django_db
def test_list_test_wrong_method():

    request = RequestFactory().put(PATH, data={})
    
    response = list_test(request)
    content = json.loads(response.content)
    
    assert content["status"] == 400

@pytest.mark.django_db
def test_list_test_invalid_login():

    request = RequestFactory().get(PATH, data={})
    
    response = list_test(request)
    content = json.loads(response.content)
    
    assert content["status"] == 500
