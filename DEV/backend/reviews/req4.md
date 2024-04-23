# REQ4

## Geral

Define param request type

Add Docstring to functions
___
## unfinished_reproved_quizzes(request)

- use guard clause instead of envolving the entire function in a if

- `token = request.headers["Authorization"]`\
can be replaced for function on utils.tokens

- remove 'try execption Exception' block\
verify if function in previous point returns None

- use guard clause in 'if verify_token(token)'

- save `Vote.objects.filter(question__id=q_id)` int temp var to not do a query 2 times

___
## vote(request)

- use guard clause instead of envolving the entire function in a if

- `token = request.headers["Authorization"]`\
can be replaced for function on utils.tokens

- remove 'try execption Exception' block\
verify if function in previous point returns None

- catch error if user votes 2 times in the question.
(yes, he can do it)

- save `Vote.objects.filter(question__id=q_id)` int temp var to not do a query 2 times
