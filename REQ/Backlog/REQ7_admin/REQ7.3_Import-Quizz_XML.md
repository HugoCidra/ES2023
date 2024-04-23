# REQ7.3 - Menu: Import Quizzes as XML

- **PRIMARY ACTOR:** User

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** Reviewers/ Users

- **PRECONDITIONS:**
1. User is logged on
2. The XML is aligned with guidelines

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** User can successfully import quizzes using XML and be guaranteed that there are no duplicates

- **MAIN SUCESS SCENARIO:** 
1. User navigates to the '/menu' present in the homepage
2. System displays the menu with an 'Import' option
3. User selects an XML file from their machine
4. User clicks 'Import'
5. The system processes and validate the XML file information (duplicate quizzes) 
6. System provides feedback: "Quizzes Successfully Imported"

- **EXTENSIONS/ALTERNATIVE PATHS:** 

3. (a) If the selected file is not in XML format:
- System provides feedback: "Invalid file format"
6. (a) If the XML file is not aligned with guidelines:
- System provides feedback: "Can't read data from XML file"


---

# Guidelines & Restrictions

- XML needs to be aligned with other PLs
