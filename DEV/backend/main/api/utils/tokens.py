from datetime import datetime, timedelta
from jwt import encode, decode, exceptions
from django.http import HttpRequest

SECRET = "JrjvV*pV7j5lpY4Xf*CTo_vsn1U*mpikYGJ9FHWHsM&xXgMOAOj%Jd#5VslxUyUzEI4lOQUQNxB#oybe56VGFT%R5p8MEA7P#30VCsm6u&eUHryW#xVt5dJwZm?UHFtld3TVKxfMgNr5h#x5njj4SJjQYYJOqUwU1KGI9OUnuUUtxLE76o5JSdG7Nh4!aRrchWEQoTzG*Kgu1YKHXWdS0_J_v0nersuDki30Nofd5eLpBmwVu53vdFzQYifVUbUGS2L7e6Fz8jbFU?3F?Y%jEmbd#Dl&DefV*Pav4v%1?akD"


def write_token(data:dict) -> bytes:
    """Generate the jwtoken

    Args:
        data (dict): information to store on the token

    Returns:
        bytes: the token in bytes
    """

    # duracao de validade do token
    expier_date = lambda time: datetime.now() + timedelta(minutes=time)
    
    # criacao do token
    token = encode(payload={**data, "exp": expier_date(60)}, key=SECRET, algorithm="HS256")
    return token.encode("UTF-8")

def verify_token(token: str, *, verify_exp=True) -> bool:
    """Verificar se token e valido ou nao

    Args:
        token (str): token para validar

    Returns:
        bool: 'True' se for valido 'False' se nao
    """

    options = {"verify_exp": verify_exp}

    try:
        # if it runs with no problem means its valid
        decode(token, key=SECRET, algorithms=["HS256"], options=options)
    except exceptions.DecodeError:
        # in case we cannot decode

        # print(token)
        return False
    except exceptions.ExpiredSignatureError:
        # in case the token validation as expired
        return False
    
    return True

def extrat_token_info(token: str, *, verify_exp=True) -> dict:
    """Extrat the stored information on the token

    Args:
        token (str): token to extrat the information of

    Returns:
        dict | None: dictionary coded on the token
    """

    options = {"verify_exp": verify_exp}
    try:
        # if it runs with no problem means its valid
        return decode(token, key=SECRET, algorithms=["HS256"], options=options)

    except exceptions.DecodeError:
        # in case we cannot decode
        return None
        
    except exceptions.ExpiredSignatureError:
        # in case the token validation as expired
        return None

def extract_token(request: HttpRequest) -> str:
    """Functions to extrat the token from the request

    Args:
        request (HttpRequest): the request from django. type (django.http.HttpRequest)

    Returns:
        str | None: return the token if its there returns 'None' otherwise
    """
    token = request.headers.get('authorization', None)
    if token is None:
        return None
    
    if token[5] == ' ':
        return token[6:]
    
    return token
