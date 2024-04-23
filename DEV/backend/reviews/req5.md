# REQ4

## Geral

Define param request type

Check if user is logged in

Add Docstring to functions
___
## def check_if_user_has_test_to_do(request)

- in '# search for test' use count() instead of all().
You are wasting memory.

___
## get_test(request)
- instead of  saving the questions and options first an then process da information, process the info whikle you are reading.
(use 'test.questions.all()' and 'question.option_set.all()' in the for loops diractly)
