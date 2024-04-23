# REQ1.2 - Register

- **PRIMARY ACTOR:** User

- **SCOPE:**  User Goals

- **STAKEHOLDER AND INTERESTS:** None

- **PRECONDITIONS:** None

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** User can register

- **MAIN SUCESS SCENARIO:**
1. User enters '/login' page (props type = 'register')
2. System shows '/login' page with "email", "Username" and "Password" boxes, 'Register' button and link to login page
3. User inputs their credentials on "eamil", "Username" and "Password" Register boxes
4. 4. User clicks 'Register' button or presses 'Enter' key
5. System redirects User to '/' page (already logged in)

- EXTENSIONS/ALTERNATIVE PATHS:

3. (a) User inputs invalid credendials on "email", "Username" and "Password" Register boxes
4. (a) 4. User clicks 'Register' button or presses 'Enter' key
5. (a) System feedback: Wrong Credentials

---

# Guidelines & Restrictions

- Valid credentials to 'email': 
1. lowercase alphanumerical characters
2. (rule1_.) + @ + (rule1) + (.(rule1){1+}) 

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

<!-- ### TEST 1.2.1
- Given: User is on '/login' page
- When:
1. User types: 'myNewUser1' on Register username box
2. User types: 'password' on Register password box 
3. User clicks Register button
- Then: System redirects to '/' page with User logged in

### TEST 1.2.2
- Given: User is on '/login' page
- When:
1. User types: 'justAUser1' on Register username box
2. User types: 'password' on Register password box 
3. User clicks Register button
- Then: System feedbacks: 'Username already exists!'

### TEST 1.2.3
- Given: User is on '/login' page
- When:
1. User types: '' on Login username box (User not registered)
2. User types: 'password' on Login password box 
3. User clicks Login button
- Then: System feedbacks: 'Username must be between 6 and 18 characters'

### TEST 1.2.4
- Given: User is on '/login' page
- When:
1. User types: 'myNewUser500' on Login username box (User not registered)
2. User types: '' on Login password box 
3. User clicks Login button
- Then: System feedbacks: 'Password must be between 6 and 18 characters' -->