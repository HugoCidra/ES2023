# REQ2.1 - Navigate to 'Create Quiz' page

- **PRIMARY ACTOR:** Creator

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** Reviewers

- **PRECONDITIONS:**
1. Creator is logged on

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** User can go from any page (except '/login') to '/create-quizz' page

- **MAIN SUCESS SCENARIO:** 
1. User enters any page (except '/login')
2. System shows page 'Create Quiz' option on Navigation Bar 
3. User clicks 'Create Quiz'
4. System redirects to '/create-quizz' page

- EXTENSIONS/ALTERNATIVE PATHS: None

---

# Guidelines & Restrictions

- None

---
### TESTS

### TEST 2.1.1
- Given: User is on any page (except '/login')
- When:
1. User clicks 'Create Quiz' button on NavBar 
- Then: System redirects to '/create-quizz' and 'Create Quiz' button on NavBar changes background to darker blue