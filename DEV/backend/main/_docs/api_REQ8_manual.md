# View manua Manual

## `get_username` Function
- **Path:** `api/REQ8/get_username/`
- **Method:** GET
- **User Auth:** Yes

### Request Format
```json
{}
```


### Response Format
```json
{
"status": 200,
"username": <str: username>
}
```


### Status Codes
- 400 -> Wrong method, invalid token or user not logged in, user doesnt exist or can't be found
- 200 -> Success

---

## `get_stats_solver` Function
- **Path:** `api/REQ8/get_tags_solver/`
- **Method:** GET
- **User Auth:** Yes

### Request Format
```json
{}
```


### Response Format
```json
{
    "status": 200,
    "data": [
        {
            "name": <str: tag_name>,
            "x": <int: number_of_correct_answers>,
            "y": <int: number_of_incorrect_answers>
        },
        {...},
        ...
    ]
}
```


### Status Codes
- 400 -> Wrong method, invalid token or user not logged in, user doesnt exist or can't be found
- 401 ->  User is not a solver
- 200 -> Success

---

## `get_tags_creator` Function
- **Path:** `api/REQ8/get_tags_creator/`
- **Method:** GET
- **User Auth:** Yes

### Request Format
```json
{}
```

### Response Format
```json
{
    "status": 200,
    "data": [
        {
            "name": <str: tag_name>,
            "x": <int: accepted_count>,
            "y": <int: rejected_count>
        },
        {
            "name": <str: tag_name>,
            "x": <int: accepted_count>,
            "y": <int: rejected_count>
        },
        ...
    ]
}
```
### Status Codes
- 400 -> Wrong method, invalid token or user not logged in, user doesnt exist or can't be found
- 200 -> Success
