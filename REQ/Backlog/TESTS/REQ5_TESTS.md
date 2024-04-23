### TEST 5.1.1

- Given: User is on '/Solve-test/' page
- When: User clicks 'CANCEL' button
- Then: System redirects to '/Home/' page and the  is not saved


### TEST 5.1.2

- Given: User is on '/Solve-test/' page
- When: User clicks 'SUBMIT' button with option selected
- Then: System redirects to '/Home/' page, " submitted" message and  is saved on the database
  
### TEST 5.1.3


- Given: User is on '/Solve-test/' page
- When: User clicks 'SUBMIT' button withou option selected
- Then: System redirects to '/Home/' page, " do you want to save" message 



### TEST 5.1.4

- Given: User is on '/Solve-test/' page
- When: User clicks 'SAVE' button
- Then: System redirects to '/Home/' page, " saved" message and  is saved as a draft on the database



### TEST 5.1.5

- Given: User is on '/Solve-test/' page
- When: User clicks 'SUBMIT' button
- Then: Only one option needs to be filled for a valid submission


### TEST 5.1.6

- Given: User is on '/Solve-test/' page
- When: User clicks 'SUBMIT' button
- Then: Justification box # has more/less caracters than the limit allowed


### TEST 5.1.7

- Given: User is on '/Solve-test/' page
- When: Front-end or back-end error occurs
- Then: System shows error message to the user



### TEST 5.1.8

- Given: User is on '/Solve-test/' page
- When: User clicks the logo
- Then: System redirects to '/Home/' page




### TEST 5.3.1

- Given: User is on '/See-test-solution/' page
- When: User clicks 'Home' button
- Then:  System redirects to '/Home/' page


### TEST 5.3.2

- Given: User is on '/See-test-solution/' page
- When: Front-end or back-end error occurs
- Then:  System shows error message to the user