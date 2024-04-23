# REQ4.2 - Reviewer Submit Vote: Reject

- **PRIMARY ACTOR:** Reviewer

- **SCOPE:  User Goals**

- **STAKEHOLDER AND INTERESTS:** Creator, Solvers

- **PRECONDITIONS:**
1. Reviewer is logged on
2. Reviewer has least one quizz to review

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** Reviewer can Vote: 'Reject' to a Quizz

- **MAIN SUCESS SCENARIO:**
1. Reviewer enters '/review-quizz' page
2. System shows page with the Question and options (with answer in green)
3. Reviewer fills the justification box
4. Reviewer clicks 'Reject'
5. Reviewer clicks 'Submit'
6. Vote is Submited and System keeps in '/review-quiz' and shows next quiz to review (if available)

- EXTENSIONS/ALTERNATIVE PATHS:

4. (a) Reviewer clicks 'Cancel' button
5. (a) System redirects to '/' page

6. (b)  System redirects to '/' page (if there are no quizzes left to review)

6. (c) (3rd vote case) System redirects to '/' page, Vote is submitted and Quizz changes state to 'rejected'

---

# Guidelines & Restrictions

- Justification is mandatory ( Character range: 40 - 512 )

- Accept / Reject a Quizz: best of 5 votes

- Page shows votation status
