# REQ5.2 - Submitted Test is saved (for future reference)

- **PRIMARY ACTOR:** Solver

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** Solvers, Creators

- **PRECONDITIONS:**
1. Solver is logged on
2. Solver has at least one available

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** Solver can submit a solved Test

- **MAIN SUCESS SCENARIO:** 
1. User enters '/solve-test/{tes_id}' page
2. System shows page with ALL information* about the 20 quizzes from the selected Test, Submit and Cancel options
3. User selects options
4. User clicks 'Submit'
5. System feedback: 'Test Completed' (and solved_test is stored)

- EXTENSIONS/ALTERNATIVE PATHS:

3. (a) Solver clicks 'Cancel' button
4. (a) System redirects to '/home' page

---

# Guidelines & Restrictions

None
