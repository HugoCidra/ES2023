from django.http import HttpRequest, JsonResponse
from django.db.utils import IntegrityError
from typing import List
import bcrypt

from ..models import User
from ..utils import tokens, requests

# helper functions
def get_values(payload: dict, keys:List[str]):
    """Get certain values from a dict

    Args:
        payload (dict): dictionary to extract the values
        keys (List[str]): name of the values to look in the dict

    Returns:
        _type_: the value of the key in the dict

    Yields:
        _type_: the value of the key in the dict
    """

    # if the numb of keys == 1 we have to return (not yield) to not give a generator
    if len(keys) == 1:
        return payload.get(keys[0], None)
    
    for i in keys:
        val = payload.get(i, None)
        yield val


# api methods
def register(request: HttpRequest):
    """Register a User in the database and retrieve a token for authentication.

    Args:
        request (HttpRequest): request

    Returns:
        _type_: None
    """
    # parameters that must be present in the request
    needed_params = ["username", "password", "email"]

    # check if method is POST (create)
    if request.method != "POST":
        return JsonResponse({'status': 405, 'log': f"Method ({request.method}) not alowed, only POST"})

    payload = requests.extract_request_params(request)
    if payload == {}:
        return JsonResponse({'status': 500, 'log': "empty / invalid body"})
        
    password: str
    name, password, email = get_values(payload, needed_params)
    
    if email is None:
        email = ''

    # check if needed parameters were given
    if None in (name, password, email):
        not_found = filter(lambda x:payload.get(x, None) is None, needed_params)

        return JsonResponse({'status': 400, 'log': f"Param(s) {', '.join(not_found)} not found"})
    
    # create user
    new_password = bcrypt.hashpw(password.encode('u8'), bcrypt.gensalt())  # hash the password with random salt
    new_user = User(name=name, password=new_password.decode('u8'), email=email)
    
    try:
        new_user.save()
    except IntegrityError:
        # because we will have to get the user in order to then get the password,
        # it cannot exist two users with the same username
        return JsonResponse({'status': 500, 'log': "Username already exists"})

    # print(new_user.id)
    return JsonResponse({'status': 200, 'token': tokens.write_token({'id': new_user.id}).decode('u8')})


def login(request: HttpRequest):
    """Verify User credentials and retrieve a token for authentication.

    Args:
        request (HttpRequest): request

    Returns:
        _type_: None
    """
    # parameters that must be present in the request
    needed_params = ["username", "password"]
    
    # check if method is PUT
    if request.method != "PUT":
        return JsonResponse({'status': 405, 'log': f"Method ({request.method}) not alowed, only PUT"})

    payload = requests.extract_request_params(request)
    if payload == {}:
        return JsonResponse({'status': 500, 'log': "empty / invalid body"})
  
    password: str
    username, password = get_values(payload, needed_params)

    try:
        user = User.objects.get(name=username)
        
        if not bcrypt.checkpw(password.encode('u8'), user.password.encode('u8')):
            raise User.DoesNotExist  # raises exception below
    except User.DoesNotExist:
        # if username cannot be found or password is wrong
        return JsonResponse({'status': 500, 'log':"Invalid credentials"})


    return JsonResponse({'status': 200, 'token': tokens.write_token({'id': user.id}).decode('u8')})
