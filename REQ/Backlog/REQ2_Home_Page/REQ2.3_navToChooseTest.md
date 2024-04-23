# REQ2.3 - Navigate to 'Choose Test' page

- **PRIMARY ACTOR:** Solver

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** None

- **PRECONDITIONS:**
1. Solver is logged on

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** User can go from any page (except '/login') to '/choose-test' page

- **MAIN SUCESS SCENARIO:** 
1. User enters any page (except '/login')
2. System shows page 'Solve Test' option on Navigation Bar 
3. User clicks 'Solve Test'
4. System redirects to '/choose-test' page

- EXTENSIONS/ALTERNATIVE PATHS: None

3. (a) User clicks 'Solve Test' (Precondition failed: User is NOT Solver)
4. (a) System feedback: User is not Solver

---

# Guidelines & Restrictions

- None

---
### TESTS

### TEST 2.3.1
- Given: Solver is on any page (except '/login')
- When:
1. User clicks 'Solve Test' button on NavBar 
- Then: System redirects to '/choose-test' and 'Solve Test' button on NavBar changes background to darker blue

### TEST 2.3.2
- Given: User not Solver is on any page (except '/login')
- When:
1. User clicks 'Solve Test' button on NavBar 
- Then: System feedbacks: 'Must be a Solver' 