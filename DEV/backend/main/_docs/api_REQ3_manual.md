# View manual

## get_quiz
- path: `api/REQ3/get-quiz/<question_id>/`
- method: GET
- user auth: True
- description: Retrieves a draft or rejected quiz through its id 
        and also the reviews if it's a rejected quiz

### Request format
```
{ }
```

### Response format
```json
{
  "success": "true",
  "code": 201,
  "message": "information collected successfully",
  "data": {
    "question": <str>,
    "opt_text": <str>,
    "tag": <str>,
    "num_tests": <int>,
    "options": [
      {
        "body": <str>,
        "is_correct": <bool>,
        "justification": <str>
      },
      {
        "body": <str>,
        "is_correct": <bool>,
        "justification":<str>
      },
      {...}
    ],
    "rejected_justifications": [
      {
        "justification": <str>
      },
      {
        "justification": <str>
      },
      {...}
    ]
  }
}

```

### Status codes
- 404 -> wrong method
- 400 -> invalid credentials
- 401 -> Unauthorized access
- 201 -> success

---
## create_quiz
- possible paths:
     - `api/REQ3/submit-quiz/`
     - `api/REQ3/save-quiz/`
- method: POST
- user auth: True
- description: Saves or submits a quiz in the database

### Request format
```
{
  "question_id": <int>;
 }
```

### Response format
```json
{
  "status": 201,
  "message": "Quiz submitted succesfully."
}
```

### Status Code
- 404 -> wrong method
- 400 -> invalid credentials
- 401 -> Unauthorized access
- 201 -> success

---
## delete_quiz
- path: `api/REQ3/delete/<question_id>/`
- method: POST
- user auth: True
- description: Delete a question and all the options with the id

### Request format
```
{ }
```

### Response format
```json
{
  "success": "true",
  "code": 200,
  "message": "Quiz deleted succesfully."
}
```

### Status Code
- 404 -> wrong method
- 400 -> invalid credentials
- 200 -> success

---
## update_quiz

- Auxiliary function that helps the function create_quiz by updating the stats of the quiz

---
## new_quiz

- Auxiliary function that helps the function create_quiz by creating a new quiz