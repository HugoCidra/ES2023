## TEST 3.1.1

- Given: User is not on '/login' page
- When: User enters the page
- Then: User is logged on


## TEST 3.1.2

- Given: Defined layouts on Repository
- When: User enters the page
- Then: Component follows the defined layout


## TEST 3.2.1

- Given: User is on '/create-quiz page
- When: User clicks 'CANCEL' button
- Then: System redirects to '/home' page


## TEST 3.2.2

- Given: User is on '/create-quiz page
- When: User clicks 'SUBMIT' button
- Then: System redirects to '/home' page and "Quiz submitted" message is shown


## TEST 3.2.3

- Given: User is on '/create-quiz' page
- When: User clicks 'SAVE' button
- Then: System redirects to '/home' page and "Quiz saved" message is shown


## TEST 3.2.4

- Given: User is on '/create-quiz' page
- When: User clicks the logo
- Then: System redirects to '/home' page


## TEST 3.3.1

- Given: User is on '/create-quiz' page and not all input boxes are filled
- When: User clicks 'SUBMIT' button
- Then: Error messge "All input boxes need to be filled for a valid submission"


## TEST 3.3.2

- Given: User is on '/create-quiz' page and onde or more input boxes have more caracters than the limit allowed
- When: User clicks 'SUBMIT' button
- Then: Error message "The number of caracters in input boxes can´t exceed the limit allowed"


## TEST 3.3.3

- Given: User is on '/create-quiz' page one or more questions have less than 6 answer options
- When: User clicks 'SUBMIT' button
- Then: Error message "Every question needs to have 6 answer options"


## TEST 3.3.4

- Given: User is on '/create-quiz' page and one or more questions have more than one equal answer
- When: User clicks 'SUBMIT' button
- Then: Error message "Questions cannot have more than one equal answer"


## TEST 3.3.5

- Given: User is on '/create-quiz' page and one or more questions don´t have a correct answer selected
- When: User clicks 'SUBMIT' button
- Then: Error message "Every question must have a correct answer selected"


## TEST 3.3.6

- Given: User is on '/create-quiz' page and one or more questions have more than one correct answer
- When: User clicks 'SUBMIT' button
- Then: Error message "Questions cannot have more than one correct answer"


## TEST 3.3.7

- Given: User is on '/create-quiz' page and not all correct answers have justifications
- When: User clicks 'SUBMIT' button
- Then: Error message "Every correct answer must have a justification"


## TEST 3.4.1

- Given: User is on '/create-quiz page
- When: User clicks 'CANCEL' button
- Then: Quiz is not saved


## TEST 3.4.2

- Given: User is on '/create-quiz' page
- When: User clicks 'SAVE' button
- Then: Quiz is saved as a draft on the database

## TEST 3.4.3

- Given: User is on '/create-quiz' page
- When: User clicks 'SUBMIT' button
- Then: Quiz is saved on the database


## TEST 3.4.4

- Given: User is on '/create-quiz' page
- When: creates anew quiz
- Then: System accepts special caracters


## TEST 3.5.1

- Given: User is on '/create-quiz' page
- When: Draf is load
- Then: User is able to change previously written boxes


## TEST 3.5.2

- Given: User is on '/create-quiz' page
- When: Draf is load
- Then: User is able to change the selected correct answer