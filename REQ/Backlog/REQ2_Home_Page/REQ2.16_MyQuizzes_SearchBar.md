# REQ2.16 - MyQuizzes SearchBar

- **PRIMARY ACTOR:** User

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** None

- **PRECONDITIONS:**
1. User is logged on
2. user has at least one quizz (draft, in evaluation, rejected, accepted)

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** Creator can see its Quizzes filtered by a substring inserted in the search box

- **MAIN SUCESS SCENARIO:** 
1. User enters '/' page
2. System shows page with 'My Quizzes' containing ALL its Quizzes, search bar and filter dropdown
3. User selects either of the states available in the filter dropdwon
4. System shows page with 'My Quizzes' containing its quizzes with the state selected
5. User selects the search bar and inserts one or more characters
6. System shows page with 'My Quizzes' containing its quizzes that contain the input on the search bar (with the state selected)

- **EXTENSIONS/ALTERNATIVE PATHS:** None

---

# Guidelines & Restrictions

- The search of the input of searchBar is only performed on the quizzes with the selected state
- The use case of the filter is defined in REQ2.15