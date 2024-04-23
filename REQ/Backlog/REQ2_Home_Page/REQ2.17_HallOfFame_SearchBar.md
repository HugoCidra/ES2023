# REQ2.17 - HallOfFame SearchBar

- **PRIMARY ACTOR:** User

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** None

- **PRECONDITIONS:**
1. User is logged on
2. There is at least one creator with one approved quiz

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** Creator can select a user of all of the creators and solvers, as referenced in [REQ2.6](./REQ2.6_show_all_Creators.md) and [REQ2.8](./REQ2.8_ShowAllSolvers.md)

- **MAIN SUCESS SCENARIO:** 
1. User enters '/' page
2. System shows page with 'Hall of Fame - Creators' -> Creators sorted by score, 'Hall of Fame - Solvers' -> Solvers sorted by score and search bar
3. User selects the search bar and inserts one or more characters
4. System shows dropdown with the users whose username contains the input on the search bar
5. User selects one of the users displayed (by clicking on the username)
6. System displays the username of the selected user in the search bar
7. System automatically scrolls 'Hall of Fame - Creators' to show selected user highlighted
8. System automatically scrolls 'Hall of Fame - Solvers' to show selected user highlighted (if user is a solver)

- **EXTENSIONS/ALTERNATIVE PATHS:** None

---

# Guidelines & Restrictions

- When the search bar is selected, if there's text previously inserted, it is cleared
- In both columns (Creators and Solvers), if the user selected is the top3 of its section, then there's no need to scroll the section
