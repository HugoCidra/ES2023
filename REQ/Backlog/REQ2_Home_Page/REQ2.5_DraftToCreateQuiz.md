# REQ2.5 - Navigate to 'Create Quiz' page (from 'Home') with a Draft

- **PRIMARY ACTOR:** Creator

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** None

- **PRECONDITIONS:**
1. Creator is logged on
2. Creator has at least one Draft

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** User can go from '/' page to '/create-quizz/{quiz_id}' page

- **MAIN SUCESS SCENARIO:**
1. User enters '/' page
2. System shows page with User's Drafts
3. User selects one Draft
4. System redirects to '/create-quizz/{quiz_id}' page

- **EXTENSIONS/ALTERNATIVE PATHS:** None

---

# Guidelines & Restrictions

- None

### TEST 2.5.1
- Given: User is on '/' page with 1 Quiz with 'Draft' state 
- When:
1. User clicks Quiz with 'Draft' state
- Then: System redirects to '/create-quizz/{quiz_id}'