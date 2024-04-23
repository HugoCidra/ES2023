# View manual

## register
- path: `api/REQ1/register/`
- method: POST
- user auth: False

### Request format
```
{
    "email": <str: email>,
    "username": <str: username>,
    "password": <str: password>
}
```

### Response format
If succeded:
```
{
    "status": 200, 
    "token": <str: token>
}
```

### Status codes
- 400 -> missing fields
- 405 -> wrong method
- 500 -> invalid body (payload) / user already exists
- 200 -> success

---
## login
- path: `api/REQ1/login/`
- method: PUT
- user auth: False

### Request format
```
{
    "username": <str: username>,
    "password": <str: password>
}
```

### Response format
If succeded:
```
{
    "status": 200, 
    "token": <str: token>
}
```
### Status Code
- 405 -> wrong method
- 500 -> invalid credentials / invalid body (payload)
- 200 -> success
---