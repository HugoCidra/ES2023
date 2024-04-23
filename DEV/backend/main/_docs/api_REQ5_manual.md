# View manual

## list_test
- path: `api/REQ5/choose-test/`
- method: GET
- user auth: True

### Request format
```
{}
```

### Response format
```
{
    "status": 200, 
    "tests": [
        {
            "id": <int: test1_id>,
            "title": <str: test1_body>,
            "tags": [
                <str: tag1>,
                <str: tag2>,
                <str: tag3>,
                <str: tag4>,
                ...
            ]
        },
        {
            "id": <int: test2_id>,
            "title": <str: test2_body>,
            "tags": [...]
        },
        {...},
        {...},
        ...
    ]
}
```
Note: tags sorted from most to least frequent in the test questions

### Status codes
- 400 -> wrong method
- 500 -> invalid credentials (dif in 'log' param)
- 200 -> success

---
## get_test
- path: `api/REQ5/get_test/`
- method: GET
- user auth: True

### Request format
```
{
    "id": <int: test_id>
}
```

### Response format
```
{
    "status": 200, 
    "questions": [
        {
            "id": <int: question1_id>,
            "body": <str: question1_body>,
            "opts": [
                {
                    "id": <int: opt1_id>,
                    "body": <str: opt1_body>
                },
                {
                    "id": <int: opt2_id>,
                    "body": <str: opt2_body>},
                {...},
                {...},
                {...},
                {...}
            ] 
        },
        {
            "id": <int: question2_id>,
            "body": <str: question2_body>
            "opts" : [...]
        }
        {...},
        {...},
        ...
    ]
}
```
Note: questions order is random

### Status Code
- 400 -> wrong method
- 500 -> invalid credentials (dif in 'log' param)
- 401 -> test not found
- 200 -> success

---
## grade_test
- path: `api/REQ5/grade_test/`
- method: POST
- user auth: True*

\* require further discussion
### Request format
```
{
    "id": <int: test_id>
    "solutions": {
        <str: question1_id>: <int: selected_q1_opt_id>,
        <str: question2_id>: <int: selected_q2_opt_id>,
        <str: question3_id>: <int: selected_q3_opt_id>,
        ...
    }
}
```
Note: "solutions" format can be converted to just a list sacrificing time efficiency.
### Response format
```
{
    "status": 200,
    "grade": <int: user_grade>,
    "results": {
        <str: question1_id>: {
            "justification": <str: selected_q1_opt_justification>
            "correct": <bool: is_the_right_option>
        },
        <str: question2_id>: {
            "justification": <str: selected_q2_opt_justification>
            "correct": <bool: is_the_right_option>
        },
        <str: question3_id>: {...},
        ...
    }
}
```

### Status Code
- 400 -> wrong method
- 500 -> invalid credentials (dif in 'log' param)
- 501 -> user already did this test
- 200 -> success
