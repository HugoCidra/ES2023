# REQ2

## Geral

Define param request type

Add Docstring to functions
___
## unfinished_reproved_quizzes(request)

- `token = request.headers["Authorization"]`\
can be replaced for function on utils.tokens

- remove 'try execption Exception' block\
verify if function in previous point returns None

- Dont pass everything of a question in the query.
Just the info that you need.

- Pass the info in format: **key: value**\
instead of list

___
## solvers(request)

- `token = request.headers["Authorization"]`\
can be replaced for function on utils.tokens

- remove 'try execption Exception' block\
verify if function in previous point returns None

- Pass the info in format: **key: value**\
instead of list

___
## creators(request)

- `token = request.headers["Authorization"]`\
can be replaced for function on utils.tokens

- remove 'try execption Exception' block\
verify if function in previous point returns None

- Pass the info in format: **key: value**\
instead of list

___
## is_solver(request)
- `token = request.headers["Authorization"]`\
can be replaced for function on utils.tokens

- remove 'try execption Exception' block\
verify if function in previous point returns None

- Pass the 'response' as bool type instead of str type
