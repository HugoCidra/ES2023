# Tokens Module

## Import the functions
```
from ..utils.tokens import *
```
or
```
from ..utils.tokens import write_token, verify_token
```
or
```
from ..utils import tokens
```
___
## Write a token
This function creates a new token given a param **data**.\
This **data** param is a python dictionary.\
The token given has a lifespan that is encoded along with the **data**.
```
def write_token(data:dict) -> bytes:

    # duracao de validade do token
    expier_date = lambda time: datetime.now() + timedelta(minutes=time)
    
    # criacao do token
    token = encode(payload={**data, "exp": expier_date(60)}, key=SECRET, algorithm="HS256")
    return token.encode("UTF-8")
```

Utilization example:
```
new_token = write_token({'name': 'Alberto', 'id': 12})
print(new_token)
```
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6OSwiZXhwIjoxNjY3MDkyNDc3fQ.c9lW_dInXXFCyavsK7rkmRk54AN1ebmIw6TO32HiHd4
```
___
## Verify a token
This function checks if the token is valid.\
A valid token its capable of decode with the **SECRET** as key
and its still in its lifespan
```
def verify_token(token: str) -> bool:
    
	try:
        # if it runs with no problem means its valid
        decode(token, key=SECRET, algorithms=["HS256"])

    except exceptions.DecodeError:
        # in case we cannot decode
        return False

    except exceptions.ExpiredSignatureError:
        # in case the token validation as expired
        return False
    
    return True
```
Utilization example:
```
def random_function(token: str):
	if verify_token(token):
		# token is valid
		# do something
	else:
		# token is not valid
		# do something else
```
___
## Extract info from token
This function extracts the **data** that was encoded in the token.\
It comes with ***'exp': \<number\>*** that is its lifespan.
```
def extrat_token_info(token: str) -> dict | None:

    try:
        # if it runs with no problem means its valid
        return decode(token, key=SECRET, algorithms=["HS256"])

    except exceptions.DecodeError:
        # in case we cannot decode
        return None

    except exceptions.ExpiredSignatureError:
        # in case the token validation as expired
        return None
```
Utilization example:
```
token = write_token({'name': 'Beatriz', 'id': 13})

info = extrat_token_info(token)
print(info)
```
```
{'name': 'Beatriz', 'id': 13, 'exp': 1667092477}
```
