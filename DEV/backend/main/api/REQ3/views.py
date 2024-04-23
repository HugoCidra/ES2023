import contextlib
from django.http import HttpRequest, JsonResponse
from django.db import transaction
from ..utils import tokens, requests
from ..models import User, Question, Option, Tag, Vote

# pip install pyspellchecker
from spellchecker import SpellChecker

spell = SpellChecker()
punct = ['?', '!', '.', ",", ":"]
blacklist = ['$', '*', '&', '#', '==', '!=', '<', '>', '<=', '>=', '!', '?']                  # In upper case

def well_written(text):
    check = text.split()

    # removes punctuation from the end of the word
    for i, word in enumerate(check):
        if word[-1] in punct and len(word) > 1:
            check.pop(i)
            word = word[:-1]
            check.insert(i, word)
        elif word[0] == '<' and word[-1] == '>':
            check.pop(i)
    
    # remove blacklisted words
    check = [ word for word in check if word.upper() not in blacklist ]

    mispelled_words = spell.unknown(check)
    if len(mispelled_words) > 0:
        return False
    
    return True


# This flag allows to get the submited question on get_quiz function
debug = 0
invalid_token = "could not extract token info."
wrong_request = "wrong_request type"

def get_quiz(request: HttpRequest, question_id: int):
    
    """ Retrieves a draft or rejected quiz through its' id 
        and also the reviews if it's a rejected quiz
       
        Args:
            request(HttpRequest): request  
            question_id(int): id of the question
        
        Returns:
            JsonResponse: HttpResponse with the quiz information in JSON format
    """
    
    if request.method != "GET":
        return JsonResponse({"status": 404, "message": wrong_request})

    # Check if the user is logged
    token = tokens.extract_token(request)

    if not tokens.verify_token(token):
        return JsonResponse({"error": {"code": 400,"message": invalid_token}})

    # Extract information from token about user
    user_info = tokens.extrat_token_info(token)

    # Search for the saved question on database
    try:
        user = User.objects.get(pk = user_info.get("id"))
        question = Question.objects.get(pk = question_id, user = user)
        options = Option.objects.filter(question = question_id)
        
    except Question.DoesNotExist:
        return JsonResponse({"status": 404, "message": "quiz not found or the quiz is owned by another user"})
    except Exception as e:
        return JsonResponse({"status": 404, "message": str(e)}) 


    tags_query = question.tags.all()
    tags = []
    for tag in tags_query:
        tags.append(tag.value)

    # Build the information dictionary
    data = {"question": question.body,
            "opt_text": question.opt_text,
            "tags": tags,
            "num_tests": question.num_tests,
            "state": question.state
            }

    # If its a rejected quiz, add the reviews
    lista_justifications = []
    if question.state == 3:
        try:
            votes = Vote.objects.filter(question = question)
            lista_justifications.extend({"justification": vote.justification} for vote in votes)
        except Vote.DoesNotExist:
            pass
        except Exception:
            return JsonResponse({"status": 401, "message": "something wrong with the reviews"})
        
    data["rejected_justifications"] = lista_justifications

    #add the options
    lista_options = []
    with contextlib.suppress(Exception):
        lista_options.extend({"body": i.body, "is_correct": i.is_correct, "justification": i.justification} for i in options)

    data["options"] = lista_options

    return JsonResponse({"success": "true", "code": 201, "message": "information colected succesfully", "data": data})


def create_quiz(request: HttpRequest, state: int):
    """
        Saves or submits a quiz in the database
        Args:
            request(HttpRequest): request with the information about the quiz 
            state(int): the state of the quiz
        
        Returns:
            JsonResponse: HtppResponse with a validation of insert or update in database
    """

    # Check if it's a post
    if request.method != "POST":
        return JsonResponse({"status": 404, "message": wrong_request})

    # Check if the user is logged
    token = tokens.extract_token(request)

    if not tokens.verify_token(token):
        return JsonResponse({"status": 400,"message": invalid_token})

    # Extract information from token about user
    user_info = tokens.extrat_token_info(token)

    try:
        user = User.objects.get(id=user_info["id"])
    except User.DoesNotExist:
        return JsonResponse({"status": 400,"message": "User not found."})

    # Extract information from request
    payload = requests.extract_request_params(request)

    # Check if the question is already in the database
    if "question_id" not in payload:
        return JsonResponse({"status": 400,"message": "question_id not provided"})
    
    #! check misspelled words !#

    if "check" in payload and payload["check"] == True:
        if not well_written(payload["body"]):
            return JsonResponse({"status": 400, "message": "Question contains misspelled words."})
        if not well_written(payload['opt_text']):
            return JsonResponse({"status": 400, "message": "Optional text contains misspelled words."})
        
        print(payload['opt_text'])

        for ind, option in enumerate(payload["options"]):
            if not well_written(option["body"]):
                return JsonResponse({"status": 400, "message": f'Option {ind+1} contains misspelled words.'})
            if not well_written(option["justification"]):
                return JsonResponse({"status": 400, "message": f'Option {ind+1}\'s justification contains misspelled words.'})

    if payload["question_id"] <= 0:

        # It's a new question
        try:
            question_text = payload["body"]
            correct_answer = None
            for opt in payload["options"]:
                if opt["is_correct"]:
                    correct_answer = opt["body"]
                    break

            existing_quizes = Question.objects.filter(body=question_text)

            for existing_quiz in existing_quizes:
                existing_correct_answer = Option.objects.filter(question_id=existing_quiz.id, is_correct=1).first().body
                if existing_correct_answer != correct_answer:
                    pass
                else:
                    return JsonResponse({"status": 400, "message": "Quiz already exists with the same correct answer."})


            new_quiz(payload, user, state)
            return JsonResponse({"status": 201, "message": "Quiz submitted succesfully."})

        except Exception as e:
            return JsonResponse({"status": 400, "message": str(e)})

    else:
        try:
            # Get the quiz and update it
            quiz = Question.objects.get(id=payload["question_id"])
            #tag = Tag.objects.get(value = payload["tag"]) 

            tags = payload["tags"]

            with transaction.atomic():
                update_quiz(payload, quiz, tags, state)
            return JsonResponse({"status": 201, "message": "Quiz submitted succesfully."})

        except Question.DoesNotExist:
            return JsonResponse({"status": 400, "message": "Quiz not found."})
        except Exception as e:
            return JsonResponse({"status": 400, "message": str(e)})


def update_quiz(payload, quiz, tags, state): 
    quiz.body = payload["body"]
    quiz.opt_text = payload["opt_text"]
    quiz.state = 2

    # Update the tags
    quiz.tags.clear()
    for tag in tags:
        tag = Tag.objects.get(value = tag)
        print("ADICIONEI_TAG:" ,tag)
        quiz.tags.add(tag)
        print("ADICIONEI_TAG_RESULT:" ,quiz.tags.all())

    quiz.num_tests = 0
    quiz.state = state
    quiz.save(update_fields=['body', 'opt_text', 'state', 'num_tests'])

    # Delete all the previous options to avoid bugs and insert the new ones
    Option.objects.filter(question = quiz).delete()    

    # Delete votes to allow a new vote
    votes = Vote.objects.filter(question = quiz)
    votes.delete()

    for opt in payload["options"]:
            option = Option(question = quiz,
                            body = opt["body"],
                            is_correct = opt["is_correct"],
                            justification = opt["justification"]
                            )
            option.save()


def new_quiz(payload, user, state):

    # if existing_quiz:
    #     existing_correct_answer = Option.objects.filter(question=existing_quiz, is_correct=True).first().body
    #     if existing_correct_answer != correct_answer:
    #         pass
    #     else:
    #         print("Debug: Quiz already exists with the same correct answer.")
    #         return JsonResponse({"status": 400, "message": "Quiz already exists with the same correct answer."})

    quiz = Question.objects.create(user=user,
                                   body=payload["body"],
                                   opt_text=payload["opt_text"],
                                   state=state,
                                   )

    for tag in payload["tags"]:
        tag = Tag.objects.get(value = tag)
        quiz.tags.add(tag)

    # Delete votes to allow a new vote
    votes = Vote.objects.filter(question = quiz)
    votes.delete()

    for opt in payload["options"]:
        Option.objects.create(question=quiz, body=opt["body"], is_correct=opt["is_correct"], justification=opt["justification"])


#TODO eliminar tags-questão
#TODO improve this view or remove it
def delete_quiz(request, question_id):
    
    """
        Delete a question and all the options with the id
        
        Args:
            request: dictionary to extrat the values 
            question_id: id of the question
        
        Returns:
            response: dictionary with a validation of insert or update in database
    """
    
    # Check if is a post
    if request.method != "POST":
        return JsonResponse({"status": 404, "message": "wrong request type"})
    
    # Check if the user is logged
    token = tokens.extract_token(request)

    if (tokens.verify_token(token)) == False:
        return JsonResponse({"error": {"code": 400,"message": invalid_token}})
    
    # Delete the question and the options
    try:
        quiz = Question.objects.get(id=question_id)
        options = Option.objects.filter(question=quiz.id)
        quiz.delete()

        for opt in options:
            opt.delete()

    except Exception as e:
        return JsonResponse({"error": {"code": 404, "message": str(e)}})

    return JsonResponse({"success": "true", "code": 200, "message": "Quiz deleted succesfully."})


""" 
SAVE E SUBMIT
{ 
    "question_id": 1,
    "body" : "teste",
    "opt_text": "texto opcional",
    "options" : [{"body":"option1", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option2", "is_correct": true, "justification":"alguma coisa"},
                {"body":"option3", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option4", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option3", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option3", "is_correct": false, "justification":"alguma coisa"}
                ],
    "tags" :   ["ES"]
} 

GET
{ 
    "question": "teste",
    "opt_text": "texto opcional",
    "tags":["ES"],
    "num_tests": 0,
    "rejected_justifications": [{"justification": "teste_rejeted_1"},
                                {"justification": "teste_rejeted_2"},
                                {"justification": "teste_rejeted_3"},
                                ]
    "options" : [{"body":"option1", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option2", "is_correct": true, "justification":"alguma coisa"},
                {"body":"option3", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option4", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option3", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option3", "is_correct": false, "justification":"alguma coisa"}
                ],
} 
"""

