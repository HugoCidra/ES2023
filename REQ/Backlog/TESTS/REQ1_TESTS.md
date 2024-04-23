## TEST 1.1.1
Given: User is on '/login' page
When: User writes username on register area
Then: System checks if username is available and follows guidelines

## TEST 1.1.2
Given: User is on '/login' page
When: User's username is unavailable/doesn't follow guidelines
Then: Error message is shown

## TEST 1.1.3
Given: User is on '/login' page
When: User writes password on register area
Then: System checks if password follow the guidelines

## TEST 1.1.4
Given: User is on '/login' page
When: User's password doesn't follow guidelines
Then: Error message is shown

## TEST 1.2.1
Given: User is on '/login' page
When: User writes username and password on login area
Then: System checks if the user is registered in the database

## TEST 1.2.2
Given: User has valid credentials
When: User clicks on 'LOGIN' button
Then: User is redirected to '/Home' page

## TEST 1.2.3
Given: User has invalid credentials
When: User clicks on 'LOGIN' button
Then: Error message is shown