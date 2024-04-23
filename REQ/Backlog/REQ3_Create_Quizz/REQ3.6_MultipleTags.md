# REQ3.2 - Create Quiz

- **PRIMARY ACTOR:** Creator

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** 
  
    Reviewers - Want to review the quiz  
    Solvers - Want to solve the quiz  

- **PRECONDITIONS:**
1. Creator is logged on

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** Creator can choose one or more TAGs when creating a new Quiz

- **MAIN SUCESS SCENARIO:**
User enters '/create-quizz' page
System shows page with all boxes * empty
3. User fills all the input boxes
4. User selects all the TAG's he wants the quiz to have
5. User clicks 'SUBMIT' button
6. System feedback: Quiz Submitted
7. System redirects to '/' page

- **EXTENSIONS/ALTERNATIVE PATHS:** None

    5\. (a) User clicks 'CANCEL' button  
    6\. (a) System redirects to '/' page

    6\. (b) User did not fill the boxes correctly  
    7\. (b) System feedbacks with error

---

# Guidelines & Restrictions

-  All boxes * : 
1. 'What's your question?' box
2. 'Optional text' box
3. 6 'Option' boxes
4. 6 'Justification' boxes
5. 6 checkboxes
6. TAG select box
