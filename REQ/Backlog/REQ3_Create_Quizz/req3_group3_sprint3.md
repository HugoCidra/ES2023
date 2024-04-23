# GROUP 3 - SPRINT 3 - REQ3
---

## Functional Tests (Manual):
1. Check if an User is logged on
2. Check if the User is redirected to /Home/ by clicking on the logo
3. Check if there is a question box
4. Check if there are 6 option boxes and 6 boxes to mark the answer
5. Check if there is a justification box
6. Check if there is a CANCEL button
7. Check if User is redirected to /Home/ page
8. Check if the quizz is not saved in the database
9. Check if there is a SAVE button
10. Check if the User is redirected to /Profile/Drafts/
11. Check if a "Quizz saved" message is shown
12. Check if the quizz is saved as a draft in the database and not as a submitted quizz
13. Check if in the case of closing the creation page the quizz is saved as a draf
14. Check is there is a SUBMIT button
15. Check is User is redirected to /Profiles/Quizzes/ if the submittion is valid or back to the creation page if there is an error
16. Check if a "Quizz submitted" message is shown
17. Check if the quizz is saved in the database
18. Check if all quizzes and drafts created by the user are saved and can be accessed
19. Check if all input boxes are filled when the quizz is submitted
20. Check if no input box has more or less caracters than the limits of that box
21. Check if the system accepts special caracters
22. Check if every question has 6 answer options
23. Check if there are no equal answers to a question
24. Check if a error message is shown if the user tries to submit a quizz without the minimum number of questions
25. Check if quizzes can be deleted or edited 
26. Check if all questions have a correct option selected when the quizz is submitted
27. Check if no question has more than one correct answer
28. Check if all questions have a justification
29. Check if error messages are shown to the user

---

## REQ3.1

REQ3.1.1: Functional 'Question' box in the /Create-quizz/ page

- DoD: Passes Tests: 3
- Owner: Rui Bernardo


REQ3.1.2: Functional 'Option and answer' boxes in the /Create-quizz/ page

- DoD: Passes Tests: 4
- Owner: Rui Bernardo


REQ3.1.3: Functional 'Justification' box in the /Create-quizz/ page

- DoD: Passes Tests: 5
- Owner: Rui Bernardo



REQ3.1.4: Functional 'CANCEL' button in the /Create-quizz/ page (front-end)

- DoD: Passes Tests: 6, 7
- Owner: João Moura


REQ3.1.5: Functional 'SAVE' button in the /Create-quizz/ page (back-end)

- DoD: Passes Tests: 9, 10, 11
- Owner: João Moura


REQ3.1.6: Functional 'SUBMIT' button in the /Create-quizz/ page (back-end)

- DoD: Passes Tests: 14, 15, 16
- Owner: João Moura


REQ3.1.7: Verification and error message: "All input boxes need to be filled for a valid submission"

- DoD: Passes Tests: 19
- Owner: João Moura


REQ3.1.8: Verification and error message: "Input box # has more/less caracters than the limit allowed" (# - box number)

- DoD: Passes Tests: 20
- Owner: Rui Bernardo


REQ3.1.9: Back-end support for special caracters

- DoD: Passes Tests: 21
- Owner: Dinu Bosii


REQ3.1.10: Verification and error message: "Every question needs to have 6 answer options"

- DoD: Passes Tests: 22
- Owner: Rui Bernardo


REQ3.1.11: Verification and error message: "Questions cannot have more than one equal answer"

- DoD: Passes Tests: 23
- Owner: João Moura


REQ3.1.12: Verification and error message: "Quizz need to have the minimum number of questions"

- DoD: Passes Tests: 24
- Owner: Rui Bernardo


REQ3.1.13: Verification and error message: "Every question must have a correct answer selected"

- DoD: Passes Tests: 26
- Owner: João Moura


REQ3.1.14: Verification and error message: "Questions cannot have more than one correct answer"

- DoD: Passes Tests: 27
- Owner: Rui Bernardo


REQ3.1.15: Verification and error message: "Every question must have a justification"

- DoD: Passes Tests: 28
- Owner: João Moura


REQ3.1.16: Front-end error messages are seen by the user

- DoD: Passes Tests: 29
- Owner: Rui Bernardo


REQ3.1.17: Back-end error messages are seen by the user

- DoD: Passes Tests: 29
- Owner: João Henriques


REQ3.1.18: Test front-end functionalities

- DoD: Report on all passing and and non-passing front-end tests
- Owner: Lino Varela


---

## REQ3.2

REQ3.2.1: Functional 'CANCEL' button in the /Create-quizz/ page (back-end)

- DoD: Passes Tests: 8
- Owner: Dinu Bosii


REQ3.2.2: Test 'CANCEL' button in the /Create-quizz/ page (back-end)

- DoD: Passes Tests: 8
- Owner: João Henriques


REQ3.2.3: Functional 'SAVE' button in the /Create-quizz/ page (back-end)

- DoD: Passes Tests: 12, 13
- Owner: João Henriques


REQ3.2.4: Test 'SAVE' button in the /Create-quizz/ page (back-end)

- DoD: Passes Tests: 12, 13
- Owner: Dino Bosii


REQ3.2.5: Functional 'SUBMIT' button in the /Create-quizz/ page (back-end)

- DoD: Passes Tests: 17
- Owner: Dinu Bosii


REQ3.2.6: Test 'SUBMIT' button in the /Create-quizz/ page (back-end)

- DoD: Passes Tests: 17
- Owner: João Henriques


REQ3.2.7: Functional /Profile/Quizzes/ page

- DoD: Passes Tests: 18
- Owner: João Moura


REQ3.2.8: Functional /Profile/Drafts/ page

- DoD: Passes Tests: 18
- Owner: Rui Bernardo


REQ3.2.9: Front-end reponse to user deleting quizz

- DoD: Passes Tests: 25
- Owner: João Moura


REQ3.2.10: Back-end reponse to user deleting quizz

- DoD: Passes Tests: 25
- Owner: Dinu Bosii



REQ3.2.11: Front-end reponse to user editing quizz

- DoD: Passes Tests: 25
- Owner: Rui Bernardo


REQ3.2.12: Back-end reponse to user editing quizz

- DoD: Passes Tests: 25
- Owner: João Henriques


REQ3.2.13: Front-end error messages are seen by the user

- DoD: Passes Tests: 29
- Owner: Rui Bernardo


REQ3.2.14: Back-end error messages are seen by the user

- DoD: Passes Tests: 29
- Owner: João Henriques