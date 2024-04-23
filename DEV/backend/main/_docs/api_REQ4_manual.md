# View manual

## quiz
- path: `api/REQ4/quiz/`
- method: GET
- user auth: True
- description: Obtains properties of a question

### Request format
```
{ }
```

### Response format
```
{
    "question": <str>,
    "options": [
       {
        "body": <str>,
        "is_correct": <bool>,
        "justification": <str>
       },
       {
        "body": <str>,
        "is_correct": <bool>,
        "justification": <str>
       },
       {...}
    ],
    "tag": <str>,
    "accepted": <int>,
    "rejected": <int>,
    "id": <int>,
    "status": 200
}


```

### Status codes
- 400 -> invalid credentials and no available quizzes
- 200 -> success

### Possible Flaws
- Doesn't handle other request method options (if a POST method is submitted it should give error 404, in the code it just handles the GET option)
- Handles error 400 on two different occasions, when there is invalid authorization and when there is no quizzes available to review. It should have 2 distinct error codes.
---
## vote
- paths: `api/REQ4/vote/`
- method: POST
- user auth: True
- description: Handles voting in a question

### Request format
```
{
    "id": "QUESTION_ID",
    "accepted": true or false,
    "value": "JUSTIFICATION"
}

```
### Response format - Question Approved
```
{
  "status": 200,
  "message": "question [QUESTION_ID] has been approved"
}
```

### Response format - Question Rejected
```
{
  "status": 200,
  "message": "question [QUESTION_ID] has been rejected"
}
```

### Response format - Vote Saved
```
{
  "status": 200,
  "message": "vote has been saved"
}
```

### Status Code
- 400 -> invalid credentials
- 200 -> success

### Possible Flaws
- Doesn't handle other request method options (if a POST method is submitted it should give error 404, in the code it just handles the GET option)
