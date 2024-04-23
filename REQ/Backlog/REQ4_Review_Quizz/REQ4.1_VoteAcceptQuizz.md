# REQ4.1 - Reviewer Submit Vote: Accept

- **PRIMARY ACTOR:** Reviewer

- **SCOPE:  User Goals**

- **STAKEHOLDER AND INTERESTS:** Creator, Solvers

- **PRECONDITIONS:**
1. Reviewer is logged on
2. Reviewer has least one quizz to review

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** Reviewer can Vote: 'Accept' to a Quizz

- **MAIN SUCESS SCENARIO:**
1. Reviewer enters '/review-quizz' page
2. System shows page with the Question and options (with answer in green)
3. (OPTIONAL STEP) Reviewer fills the justification box
4. Reviewer clicks 'Accept'
5. Reviewer clicks 'Submit'
6. Vote is Submited and System keeps in '/review-quiz' and shows next quiz to review (if available)

- EXTENSIONS/ALTERNATIVE PATHS:

4. (a) Reviewer clicks 'Cancel' button
5. (a) System redirects to '/' page

6. (b)  System redirects to '/' page (if there are no quizzes left to review)

6. (c) (3rd vote case) System redirects to '/' page, Vote is submitted and Quizz changes state to 'accepted'

6. (d) (3rd vote case & 3rd accepted case) System redirects to '/' page, Vote is submitted, Quizz changes state to 'accepted', User changes role to 'Solver'
---

# Guidelines & Restrictions

- Justification is optional

- Accept / Reject a Quizz: best of 5 votes

- Page shows votation status
