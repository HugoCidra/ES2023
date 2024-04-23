A base de dados contém 7 tabelas principais: api_user, api_tag, api_question, api_option, api_test, api_solvedtest e api_vote refletidas nos modelos User, Tag, Question, Option, Test, SolvedTest e Vote (ver DEV > backend > main > api > models.py), respetivamente.

Todas as tabelas, inclusivamente as intermédias geradas devido a relações ManyToMany, contêm um atributo id que é PK e auto-increment.

As relações ManyToMany presentes na base de dados ocorrem entre as tabelas: api_test e api_question; api_test e api_tag; api_solvedtest e api_option. 

Para ser possível o aparecimento do atributo id mencionado anteriormente no modelo físico desenhado com recurso à ferramenta onda.dei.uc.pt foi necessário criar as tabelas intermédias destas relações logo no modelo conceptual.

Descrição das tabelas principais e suas relações:

 - User:
	Atributos: name (unique), password, email, role (creator (1) ou solver(2))
	Relações: tem 0 ou mais Votes, 0 ou mais Questions, 0 ou mais Tests e 0 ou mais SolvedTests

 - Tag:
	Atributos: valor (unique)
	Relações: está associada a 0 ou mais Questions e a 0 ou mais Tests

 - Question:
	Atributos: body, opt_text, explanation, state (not_submitted(1), in_evaluation(2), rejected(3), accepted(4)), num_tests, api_tag_id (FK), api_user_id (FK)
	Relações: tem 1 ou mais Options, 0 ou mais Votes, 1 Tag, pode estar em 0 ou mais Tests, associada a 1 User (creator)

 - Option:
	Atributos: body, is_correct, justification, api_question_id(FK)
	Relações: pertence a 1 Question, pode ocorrer em 0 ou mais SolvedTests
 
- Test: 
	Atributos: title, api_user_id(FK)
	Relações: tem 1 ou mais Questions, 1 ou mais Tags, 0 ou mais SolvedTests e 1 User

 - SolvedTest:
	Atributos: grade, api_test_id(FK), api_user_id(FK)
	Relações: tem 1 ou mais Options, 1 Test e 1 User

 - Vote:
	Atributos: is_approved, justification, api_question_id(FK), api_user_id(FK)
	Relações: efetuado por 1 User, sobre 1 Question


Para além destas tabelas principais existem várias outras que são geradas automaticamente pelo Django e que não estão espelhadas no modelo apresentado.

Os índices criados para a base de dados correspondem às FK das tabelas e suas combinações. Esta criação é feita automaticamente pelo Django.