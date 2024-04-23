# Unit Tests

# REQ1

## 1. [Test_get_values.py](./REQ1/Test_get_values.py)

    Test Description
    - Test if function successfully returns certain values from a dict

    Test Steps
    - one key, key already exists
    - one key, key doesn't exist
    - multiple keys, they all exist
    - multiple keys, only some keys exist
    - multiple keys, none exists

    Data required


## 2. [test_login.py](./REQ1/test_login.py)

    Test Description
    - Test successful login 

    Test Steps
    - test_login_successful
    - test_login_invalid_credentials
    - test_login_wrong_method
    - test_login_empty_body

    Data required
    - User Creator/Default * 1


## 3. [test_register.py](./REQ1/test_register.py)

    Test Description
    - Test successful registration of a new User

    Test Steps
    - test_register_invalid_method
    - test_register_empty_payload
    - test_register_missing_username
    - test_register_missing_password
    - test_register_missing_multiple_properties
    - test_register_missing_email
    - test_register_duplicated_user
    - test_register_ok

    Data required
    - User Creator/Default * 1


# REQ2

## 1. [test_unfinished_reproved_quizzes.py](./REQ2/test_unfinished_reproved_quizzes.py)

    Test Description
    - Test if the function correctly returns all Quizzes belonging to a certain User

    Test Steps
    - test_register_invalid_method
    - test_invalid_token
    - test_valid_token

    Data required
    - User Creator/Default * 1
    - Any Quiz * 1


## 2. [test_solvers.py](./REQ2/test_solvers.py)

    Test Description
    - Test if the function correctly returns all quiz solvers

    Test Steps
    - test_solvers_invalid_method
    - test_solvers_no_token
    - test_solvers_valid_token_valid_request

    Data required
    - User Creator/Default * 1
    - User Solver * 1


## 3. [test_creators.py](./REQ2/test_creators.py)

    Test Description
    - Test if the function correctly returns all quiz creators

    Test Steps
    - test_creators_invalid_method
    - test_creators_no_token
    - test_creators_valid_token_valid_request

    Data required
    - User Creator/Default * 1


## 4. [test_is_solver.py](./REQ2/test_is_solver.py)

    Test Description
    - Test if a user is a solver

    Test Steps
    - test_is_solver_invalid_method
    - test_is_solver_invalid_token
    - test_is_solver_invalid_user
    - test_is_solver_valid_user


    Data required
    - User Creator/Default * 1
    - User Solver * 1


# REQ3

## 1. [test_create_quiz.py](pl1/DEV/testing/unit_testing/REQ3/test_create_quiz.py)

    Test Description
    - Test creation of new quiz/update of existing quiz

    Test Steps
    - test_wrong_method
    - test_invalid_token
    - test_user_not_found
    - test_question_id_not_provided
    - test_question_not_found
    - test_new_question_successful
    - test_update_question_successful

    Data required
    - User Creator/Default * 1
    - Any Quiz * 1
    - Tag * 1


## 2. [test_update_quiz.py](pl1/DEV/testing/unit_testing/REQ3/test_update_quiz.py)

    Test Description
    - Test if the update of a quiz is successful

    Test Steps
    - test_empty_payload
    - test_verify_question_deletion

    Data required
    - User Creator/Default * 1
    - Any Quiz * 1
    - Tag * 1
    - Option * 1


## 3. [test_new_quiz.py](./REQ3/test_new_quiz.py)

    Test Description
    - Test insertion of a new quiz into the database

    Test Steps
    - test_empty_payload
    - test_verify_question_creation
    - test_verify_option_creation


    Data required
    - User Creator/Default * 1
    - Tag * 1


## 4. [test_delete_quiz.py](./REQ3/test_delete_quiz.py)

    Test Description
    - Test deletion of a quiz from the database

    Test Steps
    - test_register_invalid_method
    - test_invalid_token
    - test_question_id_not_valid
    - test_delete_question_successful
    - test_verify_question_deletion

    Data required
    - Any Quiz * 1


## 5. [test_get_quiz.py](./REQ3/test_get_quiz.py)

    Test Description
    - Test retrieval of a quiz from the database

    Test Steps
    - test_get_quiz_invalid_method
    - test_get_quiz_invalid_token
    - test_get_quiz_invalid_user
    - test_get_quiz_invalid_question_id
    - test_get_quiz_not_editable
    - test_get_quiz_successful

    Data required
    - User Creator/Default * 1
    - Question not editable* 1
    - Question editable * 1


# REQ4

## 1. [test_quiz.py](./REQ4/test_quiz.py)

     Test Description
    - Test selection of random quiz to review

    Test Steps
    - test_quiz_invalid_method
    - test_quiz_invalid_token
    - test_quiz_valid_token_no_json
    - test_quiz_valid_token_no_json 

    Note
    - Function name duplicated
    - Line38, change id from 1 to -1
    - 1st test_quiz_valid_token_no_json should not return 200


    Data required
    - User Creator/Default * 1


## 2. [test_vote.py](./REQ4/test_vote.py)

     Test Description
    - Test vote registration

    Test Steps
    - test_without_token
    - test_invalid_token
    - test_verify_vote_creation
    - test_rejected_question
    - test_approved_question


    Data required
    - User Creator/Default * 4
    - Quiz 4_accepted * 2
    - Quiz 2_in_evaluation * 2
    - Vote Quiz3 * 2
    - Vote Reject Quiz4 *2


# REQ5

## 1. [test_get_test.py](./REQ5/test_get_test.py) 

     Test Description
    - Test selection of a test and its questions+options

    Test Steps
    - test_get_test_passed
    - test_get_test_not_found
    - test_get_test_wrong_method
    - test_get_test_invalid_login

    Note
    Line 72 change id from 1 to -1


    Data required
    - User Creator/Default * 1
    - Test * 1


## 2. [test_list_test.py](./REQ5/test_list_test.py) 

     Test Description
    - Test selection of all unsolved tests of a user

    Test Steps
    - test_list_test_passed
    - test_list_test_wrong_method
    - test_list_test_invalid_login

    Note
    - Test what happens if the id user does not exist (user_id = -1)

    Data required
    - User Creator/Default * 1
    - Test * 2


## 3. [test_grade_test.py](./REQ5/test_grade_test.py) 

     Test Description
    - Test registration of user options and calculate grade

    Test Steps
    - test_invalid_method
    - test_invalid_login
    - test_already_done
    - test_grade_success
  

    Note
    - Finish test_grade_success
    - what is the "user_info" passed in test_list_test_passed?
    - Test what happens if the id user does not exist (user_id = -1)
    - Test what happens if the id test does not exist (test_id = -1)

    Data required
    - User Solver * 1
    - Test * 2
    - Solved Test* 1


# REQ6

## 1. [test_create_test.py](./REQ6/test_create_test.py) 

     Test Description
    - Test test creation

    Test Steps
    - test_invalid_token
    - test_valid_token_emptytags
    - test_valid_token_not_enough_questions
    - test_created_successfully

    Note
    - Test what happens if the id user does not exist (user_id = -1)

    Data required
    - User Creator/Default * 1
    - Tag * 3 ('PM' , 'PA', 'PC')
    - Quiz 4_accepted 'PM' *10 + 'PA' * 10
    - Quiz 4_accepted 'PB' * 1


## 2. [test_tags.py](./REQ6/test_tags.py)

    Test Description
    - Test retrieval of tags from the database

    Test Steps
    - test_get_tags_invalid_method
    - test_get_tags_invalid_token
    - test_get_tags_successful

    Data required
    - Tag * 2


# REQ7

## 1. [test_load_info.py](./REQ7/test_load_info.py)

    Test Description
    - Test retrieval of user information from file

    Test Steps
    - test_load_info_successful~

    Note
    - Test method
    - Test token
    - Test Expired token
    - Test wrong question format
    - Test wrong tags format

    Data required
    - User Creator/Default * 1


## 2. [test_send_info.py](./REQ7/test_send_info.py)

    Test Description
    - Test sending of user information to file

    Test Steps
    - test_send_info_successful

    Note
    - Test method
    - Test token
    - Test Expired token

    Data required
    - User Creator/Default * 1


# REQ8

## 1. [test_get_username.py](./REQ8/test_get_username.py)

    Test Description
    - Test retrieval of username from database

    Test Steps
    - test_get_username_invalid_method
    - test_get_username_invalid_token
    - test_get_username_successful

    Data required
    - User Creator/Default * 1


## 2. [test_get_stats_solver.py](./REQ8/test_get_stats_solver.py)

    Test Description
    - Test retrieval of solver statistics from database

    Test Steps
    - test_get_stats_solver_invalid_method
    - test_get_stats_solver_invalid_token
    - test_get_stats_solver_successful

    Data required
    - User Solver * 1


## 3. [test_get_tags_creator.py](./REQ8/test_get_tags_creator.py)

    Test Description
    - Test retrieval of creator tags from database

    Test Steps
    - test_get_tags_creator_invalid_token
    - test_get_tags_creator_invalid_user
    - test_get_tags_creator_successful

    Data required
    - User Creator/Default * 1