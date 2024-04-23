import pytest
from django.test import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from api.models import User  
from api.utils import tokens
from api.REQ7.views import load_info
import json



def test_invalid_method():

    request = RequestFactory().get('/load_info', data={})
    
    response = load_info(request)
    content = json.loads(response.content)
    
    assert content["status"] == 405
    assert content["log"] =='Method (GET) not alowed, only POST'

def test_no_token():

    request = RequestFactory().post('/load_info')

    response = load_info(request)
    content = json.loads(response.content)
    
    assert content["status"] == 500
    assert content["log"] =='User not loged in'    

def test_invalid_token():

    invalid_token = "invalid_token"
    header = {"HTTP_AUTHORIZATION":invalid_token}
    request = RequestFactory().post('/load_info', **header)

    response = load_info(request)
    content = json.loads(response.content)
    
    assert content["status"] == 500
    assert content["log"] =='Expired session'

def test_invalid_file_type():
    token = tokens.write_token({'id': 1}).decode('u8')
    request = RequestFactory().post('/load_info')
    request.META['HTTP_AUTHORIZATION'] = token
    request.FILES['file']=SimpleUploadedFile('file.txt',b'invalid file',content_type="application/txt")
    
   
    response = load_info(request)
    content = json.loads(response.content)
    
    assert content["status"] == 505    

@pytest.mark.django_db    
def test_invalid_format_perguntas():
    token = tokens.write_token({'id': 1}).decode('u8')
    
    with open('REQ7/invalid_format_perguntas.xml', 'rb') as file:
        xml_data = file.read()


    request = RequestFactory().post('/load_info')
    request.META['HTTP_AUTHORIZATION'] = token
    request.FILES['file']=SimpleUploadedFile('file.xml',xml_data,content_type="application/xml")
    
   
    response = load_info(request)
    content = json.loads(response.content)
    
    assert content["status"] == 505  
    assert content['log']=='wrong format in perguntas'     

@pytest.mark.django_db    
def test_wrong_number_options():
    token = tokens.write_token({'id': 1}).decode('u8')
    
    with open('REQ7/wrong_number_options.xml', 'rb') as file:
        xml_data = file.read()


    request = RequestFactory().post('/load_info')
    request.META['HTTP_AUTHORIZATION'] = token
    request.FILES['file']=SimpleUploadedFile('file.xml',xml_data,content_type="application/xml")
    
   
    response = load_info(request)
    content = json.loads(response.content)
    
    assert content["status"] == 505  
    assert content['log']=='Question with wrong number of options'

@pytest.mark.django_db    
def test_repeated_option():
    token = tokens.write_token({'id': 1}).decode('u8')
    
    with open('REQ7/repeated_option.xml', 'rb') as file:
        xml_data = file.read()


    request = RequestFactory().post('/load_info')
    request.META['HTTP_AUTHORIZATION'] = token
    request.FILES['file']=SimpleUploadedFile('file.xml',xml_data,content_type="application/xml")
    
   
    response = load_info(request)
    content = json.loads(response.content)
    
    assert content["status"] == 505  
    assert content['log']=='Repeated Option in a Question in XML' 

@pytest.mark.django_db    
def test_repeated_question():
    token = tokens.write_token({'id': 1}).decode('u8')
    
    with open('REQ7/repeated_question.xml', 'rb') as file:
        xml_data = file.read()


    request = RequestFactory().post('/load_info')
    request.META['HTTP_AUTHORIZATION'] = token
    request.FILES['file']=SimpleUploadedFile('file.xml',xml_data,content_type="application/xml")
    
   
    response = load_info(request)
    content = json.loads(response.content)
    
    assert content["status"] == 505  
    assert content['log']=='Repeated Question in XML'     

@pytest.mark.django_db
def test_invalid_format_tags():
    token = tokens.write_token({'id': 1}).decode('u8')
    
    with open('REQ7/invalid_format_tags.xml', 'rb') as file:
        xml_data = file.read()
    
    request = RequestFactory().post('/load_info')
    request.META['HTTP_AUTHORIZATION'] = token
    request.FILES['file']=SimpleUploadedFile('file.xml',xml_data,content_type="application/xml")
    
   
    response = load_info(request)
    content = json.loads(response.content)
    
    assert content["status"] == 505  
    assert content['log']=='wrong format in tags'       

@pytest.mark.django_db #enables database access
def test_valid_format():
    token = tokens.write_token({'id': 1}).decode('u8')
    
    with open('REQ7/valid_format.xml', 'rb') as file:
        xml_data = file.read()
    

    request = RequestFactory().post('/load_info')
    request.META['HTTP_AUTHORIZATION'] = token
    request.FILES['file']=SimpleUploadedFile('file.xml',xml_data,content_type="application/xml")
    
   
    response = load_info(request)
    content = json.loads(response.content)
    
    assert content["status"] == 200    
