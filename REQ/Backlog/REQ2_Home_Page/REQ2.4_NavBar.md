# REQ2.4 - Navigation Bar 

- **PRIMARY ACTOR:** User

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** None

- **PRECONDITIONS:**
1. User is logged on

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** 
- User can see Navigation Bar with current page highlighted (except in '/') and can consult its username by clicking on the menu icon

- **MAIN SUCESS SCENARIO:**
1. User enters any page (except '/login' and '/register')
2. System shows page with Navigation Bar with current page higlighted (except in '/'')
3. User clicks on the menu icon (Img = DEV > frontend > src > IMAGES > Menu.png) to consult the username, import quiz, export quiz and perform logout 

- **EXTENSIONS/ALTERNATIVE PATHS:** None

---

# Guidelines & Restrictions

- None

---
### TESTS

### TEST 2.1.1
- Given: User is on any page (except '/login' and '/register')
- When:
1. User clicks 'Create Quiz' button on NavBar 
- Then: System redirects to '/create-quizz' and 'Create Quiz' button on NavBar changes background to darker blue

### TEST 2.2.1
- Given: User is on any page (except '/login' and '/register')
- When:
1. User clicks 'Review Quiz' button on NavBar 
- Then: System redirects to '/review-quizz' and 'Review Quiz' button on NavBar changes background to darker blue

### TEST 2.3.1
- Given: Solver is on any page (except '/login' and '/register')
- When:
1. User clicks 'Solve Test' button on NavBar 
- Then: System redirects to '/choose-test' and 'Solve Test' button on NavBar changes background to darker blue
