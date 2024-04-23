# View manual

## unfinished_reproved
- path: `api/REQ2/unfinished_reproved/`
- method: GET
- user auth: True
- description: returns the quizzes that the user didn't finish/approved

### Request format
```
{ }
```

### Response format
```
{
    "status": 200,
    "unfinished_reproved_quizzes": [
        {
            "id": <int>,
            "state": <int>",
            "tag__value": <string>,
            "body": <string>
        },
        {...},
        ...
    ]
}

```

### Status codes
- 404 -> wrong method
- 400 -> invalid credentials
- 200 -> success

---
## solvers
- path: `api/REQ2/solvers/`
- method: GET
- user auth: True
- description: returns the top 10 ranking of users that solved quizzes (ordered by their score)

### Request format
```
{ }
```

### Response format
```
{
    "status": 200, 
    "solvers": [
        {
            "user__name": <str>,
            "score": <int>
        },
        {...},
        ...
    ]
}
```
Note: the users and their respective scores are ordered by the scores. The list is limited to 10 entries only.

### Status Code
- 404 -> wrong method
- 400 -> invalid credentials
- 200 -> success

---
## creators
- path: `api/REQ2/creators/`
- method: GET
- user auth: True
- description: returns a top 10 list of quiz creators (ordered by their score)
### Request format
```
{ }
```

### Response format
```
{
   "status": 200, 
   "creators": [
        {
            "user__name": <str>,
            "score": <int>
        },
        {...},
        ...
    ]
}
```

### Status Code
- 404 -> wrong method
- 400 -> invalid credentials
- 200 -> success

---
## is_solver
- path: `api/REQ2/is_solver/`
- method: GET
- user auth: True
- description: returns True if the user role is solver (role == 2), if not, returns False

### Request format
```
{ }
```

### Response format
```
{
    "status": 200,
    "response": <True/False>
}
```

### Status Code
- 404 -> wrong method
- 400 -> invalid credentials
- 200 -> success
