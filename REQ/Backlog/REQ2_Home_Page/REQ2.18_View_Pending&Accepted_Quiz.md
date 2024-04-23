# REQ2.18 - View Pending & Accepted Quiz

- **PRIMARY ACTOR:** Creator

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** None

- **PRECONDITIONS:**
1. Creator is logged on
2. Creator has at least one Pending or Accepted quiz

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** User can go from '/' page to '/create-quizz/{quiz_id}' page, with input fields blocked

- **MAIN SUCESS SCENARIO:**
1. User enters '/' page
2. System shows page with User's Pending or Accepted quizzes
3. User selects one Pending or Accepted Quiz
4. System redirects to '/create-quizz/{quiz_id}' page, with input fields blocked

- **EXTENSIONS/ALTERNATIVE PATHS:** None

---

# Guidelines & Restrictions

- The input fields are blocked because the quizzes with state Pending or Accepted are not editable

