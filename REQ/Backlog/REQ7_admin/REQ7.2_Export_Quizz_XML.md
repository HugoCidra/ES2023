# REQ7.2 - Menu: Export Quizzes as XML

- **PRIMARY ACTOR:** User

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** Users

- **PRECONDITIONS:**
1. User is logged in
2. There is at least one quiz available for export

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** User will have in his local machine a .xml file with his quizzes

- **MAIN SUCESS SCENARIO:** 
1. User navigates to the '/menu' button present in the homepage
2. System displays the menu with an 'Export' option
3. User selects 'Export'
4. The system generates an XML file containing all quizzes
5. The system initiates the download of the XML file with all quizzes

- **EXTENSIONS/ALTERNATIVE PATHS:**

4. (a) Precondition 'At least one Quizz to export' fails -> System feedbacks

---

# Guidelines & Restrictions

- XML needs to be aligned with other PLs

