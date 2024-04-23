## TEST 2.1

Given: User is on '/' page
When: User clicks 'NEW QUIZZ' button
Then: System redirects to '/create-quizz' page

## TEST 2.2

Given: User is on '/' page
When: User clicks 'REVIEW QUIZZ' button
Then: System redirects to '/review-quizz' page

## TEST 2.3.1

Given: Solver  is on '/' page
When: Solver clicks 'SOLVE TEST' button
Then: System redirects to '/solve-test' page

## TEST 2.3.2

Given: User (!SOLVER) is on '/' page
When: User (!SOLVER) clicks 'SOLVE TEST' button
Then: System show error message 

## TEST 2.4.1

Given: User is on '/' page
When: System loads page
Then: System shows ALL User's Unfinished/Reproved quizzes (with Edit button)

## TEST 2.4.2

Given: User is on '/' page
When: User clicks 'Edit' button
Then: System redirects to '/create-quizz' page

## TEST 2.4.3

Given: Backend server is running on localhost:8000
When: url = 'http://localhost:8000/api/REQ2/unfinished_reproved/'
Then: Show all unfinished / reproved quizzes

## TEST 2.5

Given: User is on '/' page
When: System loads page
Then: System shows ALL Solvers (name & score) sorted by score

## TEST 2.5.1

Given: Backend server is running on localhost:8000
When: url = 'http://localhost:8000/api/REQ2/solvers/'
Then: Show all solvers

## TEST 2.6

Given: User is on '/' page
When: System loads page
Then: System shows ALL Creators (name & score) sorted by score

## TEST 2.6.1

Given: Backend server is running on localhost:8000
When: url = 'http://localhost:8000/api/REQ2/creators/'
Then: Show all creators