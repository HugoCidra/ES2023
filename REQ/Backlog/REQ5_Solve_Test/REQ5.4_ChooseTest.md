# REQ5.4 - Solver can choose the Test to solve 

- **PRIMARY ACTOR:** Solver

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** Solvers

- **PRECONDITIONS:**
1. Solver is logged on
2. Solver has at least one test available

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** Solver can select 1 test

- **MAIN SUCESS SCENARIO:** 
1. User enters '/choose-test' page
2. System shows page with Tests (show TAGS and Title of the every test)
3. Solver selects 1 test
4. System redirects to '/solve-test/{test_id}' page

- **EXTENSIONS/ALTERNATIVE PATHS:** None

---

# Guidelines & Restrictions

None