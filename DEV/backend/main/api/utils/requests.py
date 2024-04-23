from django.http import HttpRequest
from typing import Any, Dict
import json

class _FakeRequest:
    def __init__(self, method: str, body: bytes = b'', params: bytes = b'') -> None:
        self.method = method
        self.body = body
        self.params = params

def extract_request_params(request: HttpRequest) -> Dict[str, Any]:
    """Functions to extrat the information encoded in the request.body or reques.params

    Args:
        request (HttpRequest): the request from django. type (django.http.HttpRequest)

    Returns:
        Dict[str, Any]: a informacao em forma de um dicionario
    """
    
    if request.method == "GET":
        return request.GET
    
    if request.method in ("POST", "PUT"):
        if request.body == b'':
            return {}
        
        try:
            resp = json.loads(request.body)
        except SyntaxError:
            print(f"reques.body with wrong format: b'{request.body.decode('u8')}'")
            return {}
        
        return resp
    
    return {}
