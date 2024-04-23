# REQ2.2 - Navigate to 'Review Quiz' page

- **PRIMARY ACTOR:** Reviewer

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** Creator

- **PRECONDITIONS:**
1. Reviewer is logged on

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** User can go from any page (except '/login') to '/review-quizz' page

- **MAIN SUCESS SCENARIO:** 
1. User enters any page (except '/login')
2. System shows page 'Review Quiz' option on Navigation Bar 
3. User clicks 'Review Quiz'
4. System redirects to '/review-quizz' page

- EXTENSIONS/ALTERNATIVE PATHS: None

---

# Guidelines & Restrictions

- None

---
### TESTS

### TEST 2.2.1
- Given: User is on any page (except '/login')
- When:
1. User clicks 'Review Quiz' button on NavBar 
- Then: System redirects to '/review-quizz' and 'Review Quiz' button on NavBar changes background to darker blue