## TEST 4.1.1
Given: User is on 'review-quizz' page
When: System loads page
Then: System shows quiz/options/vote tally

## TEST 4.1.2
Given: User's justification is not between 30 and 512 characters long
When: User clicks 'Submit' button
Then: System shows error: 'justification must be between 30 and 512 characters long'

## TEST 4.1.3
Given: User hasn't clicked 'Accept' or 'Reject'
When: User clicks 'Submit' button
Then: System shows error: 'must specify vote: acception or rejection'

## TEST 4.1.4
Given: User has clicked 'Accept' button
When: User clicks 'Submit' button
Then: System requests the creation of an acception vote

## TEST 4.1.5
Given: User has clicked 'Reject' button
When: User clicks 'Submit' button
Then: System requests the creation of a rejection vote

## TEST 4.1.6
Given: User submits a valid vote
When: Frontend receives HTTP response from backend
Then: System shows success/error message

## TEST 4.1.7
Given: User is on '/review-quizz' page
When: User clicks on 'CANCEL' button
Then: System cancels review; user is routed to the home page


## TEST 4.2.1
Given: Backend server is running on localhost:800
When: GET request to 'localhost:800/api/REQ4/quiz'
Then: System responds with info on a randomly chosen available quiz

## TEST 4.2.2
Given: Backend server is running on localhost:800
When: POST request to 'localhost:800/api/REQ4/vote'
Then: System creates a Vote instance, and updates quiz status if needed
