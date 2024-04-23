# REQ1.1 - Login

- **PRIMARY ACTOR:** User

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** None

- **PRECONDITIONS:**
1. User is already registered

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** User can login

- **MAIN SUCESS SCENARIO:** 
1. User enters '/login' page (props type = 'login')
2. System shows '/login' page with "Username" and "Password" boxes, 'Login' button and link to register page
3. User inputs their credentials on "Username" and "Password" Login boxes
4. User clicks 'Login' button or presses 'Enter' key
5. System redirects User to '/' page (already logged in)

- **EXTENSIONS/ALTERNATIVE PATHS:**

3. (a) User inputs invalid credendials on "Username" and "Password" login boxes
4. (a) User clicks 'Login' button or presses 'Enter' key
5. (a) System feedback: Wrong Credentials

---

# Guidelines & Restrictions

- Valid credentials to 'Username': 
1. #characters range: 6 - 18
2. alphanumerical characters, '-', '_', ' '

- Valid credentials to 'Password':
1. #characters range: 8 - 18 
2. alphanumerical characters, '-', '_', '#', '$', '%', '&', '@'

- New user default roles: Creator (Creator includes Reviewer and Admin) 
- A Creator needs 3 accepted quizzes to become a Solver (Solver includes every other role)

- Login is valid for 60 min

---
## TESTS
<!-- 
### TEST 1.1.1
- Given: User is on '/login' page
- When:
1. User types: 'justAUser1' on Login username box
2. User types: 'admin123' on Login password box 
3. User clicks Login button
- Then: System redirects to '/' page with User logged in

### TEST 1.1.2
- Given: User is on '/login' page
- When:
1. User types: 'justAUser1' on Login username box
2. User types: 'thisIsATest' on Login password box 
3. User clicks Login button
- Then: System feedbacks: 'Invalid Credentials!'

### TEST 1.1.3
- Given: User is on '/login' page
- When:
1. User types: 'ThisIsATest' on Login username box (User not registered)
2. User types: 'thisIsATest' on Login password box 
3. User clicks Login button
- Then: System feedbacks: 'Invalid Credentials!'

### TEST 1.1.4
- Given: User is on '/login' page
- When:
1. User types: '' on Login username box (User not registered)
2. User types: '' on Login password box 
3. User clicks Login button
- Then: System feedbacks: 'Invalid Credentials!' -->