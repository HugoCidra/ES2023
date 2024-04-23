# REQ3

## Geral

Add Docstring to functions

!!! Save_question and submitQuiz are the same function apart from one param tha can be passed as a request param fom the frontend
___
## save_question(request: HttpRequest)

### # Check if the user is logged
- `token = request.headers["Authorization"]`\
can be replaced for function on utils.tokens

- remove 'try execption Exception' block\
verify if function in previous point returns None

### # Check if the question is already in the database
- 'if not question' block never enters

### # It's a new question 
- user is always a creator. Even if its solve is still a creator too.

___
## submitQuiz(request)

### # Check if the user is logged
- `token = request.headers["Authorization"]`\
can be replaced for function on utils.tokens

- remove 'try execption Exception' block\
verify if function in previous point returns None
