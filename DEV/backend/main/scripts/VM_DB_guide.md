# DataBase script para VM

## De modo a ter um ‘backup’ de vários users e quizzes criar-se-á um script  init_db_VM.py com 15 users e 140 quizzes.

### Descricao dos elementos que devem estar no script:
* Users (15):
    - Role: creator
    - Username: nomes simples (nao usar 'user_testX)
    - Password: igual para todos (nao divulgar a password!!)
    ---
    - Cada user tem de ter 1 quiz accepted
    ---
    ```python
        new_password = bcrypt.hashpw("INSERT".encode("u8"), bcrypt.gensalt())
        new_user = User(
            name="INSERT",
            password=new_password.decode("u8"),
            email="INSERT@gmail.com",
            role=1,
        )
        new_user.save()
    ```
---
* Quizzes (140):
  -  Os quizzes devem ser lógicos e de acordo com a tag
  -  Grupo3: criar 50 quizzes (pending)
  -  Todos os membros da turma: criar 3 quizzes cada (pending)
  ---
  - os últimos 10 users ficam c 1 quiz cada
  - os primeiros 5 ficam com os restantes quizzes
  ---
  ```python
  # quiz pending
    """
    tag: "ES", "AC", "BD", "COMP", "IPRP", "POO", "PPP", "RC", "SI", "SO", "TC", "TI"
    body: question text
    options > body: option text
    options > is_correct: choose ONLY ONE option as true
    options > justification: justification text
    User.objects.get(id=1):  (manter id=1)
    """
    new_quiz(
        {
            "tag": "ES",
            "body": "BODY_1",
            "opt_text": "",
            "options": [
                {
                    id: 1,
                    "body": "OPTION1",
                    "is_correct": False,
                    "justification": "JUSTIFICATION1",
                },
                {
                    id: 2,
                    "body": "OPTION2",
                    "is_correct": False,
                    "justification": "JUSTIFICATION2",
                },
                {
                    id: 3,
                    "body": "OPTION3",
                    "is_correct": False,
                    "justification": "JUSTIFICATION3",
                },
                {
                    id: 4,
                    "body": "OPTION4",
                    "is_correct": True,
                    "justification": "JUSTIFICATION4",
                },
                {
                    id: 5,
                    "body": "OPTION5",
                    "is_correct": False,
                    "justification": "JUSTIFICATION5",
                },
                {
                    id: 6,
                    "body": "OPTION6",
                    "is_correct": False,
                    "justification": "JUSTIFICATION6",
                },
            ],
        },
        User.objects.get(id=1),
        2,
    )
  ```

---
* Votes:
  - criar votos accept de modo a que os primeiros 5 users tenha 3quizzes accepted (passar a solver)
  - + 30 quizzes accepted
  - total: 45 quizzes accepted -> 135 votes accepted
  ---
  - User 1 será usado para a DEMO!! Deve ter 20 quizzes (pelo menos 3 accepted)
```python
#3 accepted votes
'''
INSERT_USER = id do 1º user a dar review (ex: INSERT_USER=3 -> users q votam: 3, 4 e 5)
INSERT_Q = id do quizz (depende da ordem q esse quiz aparece no script)
'''
 for i in range(3):
        v = Vote(
            user_id= INSERT_USER + i, is_approved=True, justification=" ", question_id= INSERT_Q
        )
        v.save()
```


---
<br><br>

### Descricao das acões a testar na VM:

* Atraves do review quiz:
  - 15 accepted
  - 10 rejected (30 justificações de rejeição)


* Atraves do new quiz:
    - 10 drafts

* Criar 2 testes
* Resolver esses 2 testes com pelo menos os primeiros 5 users (solvers)
* Verificar como ficam os profiles destes users
  
    ---
* O user 1 devera ter os 4 tipos de quizzes criados por si