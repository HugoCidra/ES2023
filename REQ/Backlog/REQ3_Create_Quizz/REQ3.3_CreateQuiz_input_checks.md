# REQ3.3 - Create Quiz (&submit) with input checks

- **PRIMARY ACTOR:** Creator

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** 
    
    Reviewers - Want to review the quiz

    Solvers - Want to solve the quiz

- **PRECONDITIONS:**
1. Creator is logged on

- **MINIMAL GUARANTEE:** None

- **SUCCESS GUARANTEE:** Creator can create a new quiz

- **MAIN SUCCESS SCENARIO:**
1. User enters '/create-quiz' page
2. System shows page
3. User fills all the input boxes *
4. User selects one or more TAGs
5. User clicks 'SUBMIT'button
6. System feedback: Quiz Submitted
7. System redirects to '/' page

- **EXTENSION/ALTERNATIVE PATHS:**

    5\. (a) User clicks 'CANCEL' button

    6\. (a) System redirects to '/' page

    6\. (b) User did not fill all the boxes correctly

    7\. (b) System feedbacks with error message

    6\. (c) User fill a box with incorrect words  

    7\. (c) System feedbacks with error message

---

# Guidelines & Restrictions

- All boxes * :
1. "What's your question?" box
2. "Optional text" box
3. 6 "Option" boxes
4. 6 "Justification" boxes
5. 6 checkboxes
6. All possible TAG boxes to select one or more of them
