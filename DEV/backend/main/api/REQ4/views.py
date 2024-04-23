from cgi import test
from itertools import count
from urllib import response
import json
from ..utils.tokens import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..models import *
import random
# Create your views here.


def quiz(request):
    """
        Handles the GET request to fetch a random quiz question for the user to vote on.
    """
    # Ensure the request method is GET
    if(request.method == 'GET'):
        try: 
            # Extract the token from the Authorization header
            token = request.headers["Authorization"]
        except Exception: 
            # Return an error status if the token is not found
            return JsonResponse({"status": 400})
        # Verify if the provided token is valid
        if verify_token(token):
            # Extract token information
            data = extrat_token_info(token)
            u_id = data["id"]
            # Fetch questions that are awaiting votes and the user hasn't voted on
            q_list = []
            q_list = list(Question.objects.exclude(user__id=u_id).filter(state=2).values_list("id", flat=True))
            v_list = list(Vote.objects.filter(user__id=u_id).values_list("question__id", flat=True))
            q_list = [x for x in q_list if x not in v_list]
            if q_list:
                # Select a random question from the list
                q_id = random.choice(q_list)
                # Prepare the response with the selected question's details
                tags_query = Question.objects.get(id=q_id).tags.all()
                tags = []
                for tag in tags_query:
                    tags.append(tag.value)
                    
                response = {}
                response["question"] = Question.objects.values_list("body", flat=True).get(id=q_id)
                response["options"] = list(Option.objects.filter(question__id=q_id).values_list("body", "justification", "is_correct"))
                response["tag"] = tags
                response["accepted"] = Vote.objects.filter(question__id=q_id).filter(is_approved=True).count()
                response["rejected"] = Vote.objects.filter(question__id=q_id).filter(is_approved=False).count()
                response["id"] = q_id
                response["status"] = 200

                return JsonResponse(response)
            else:
                # Return an empty JSON if there are no suitable questions
                return JsonResponse({})
        else:
            # Return an error status if there are no quizzes available to review
            return JsonResponse({"status": 400, "errors": "No quizzes available to review."})


def vote(request):
    """
       Handles the POST request to save a user's vote for a specific question.
    """
    # Ensure the request method is POST
    if request.method == 'POST':
        try:
            # Extract the token from the Authorization header
            token = request.headers["Authorization"]
        except Exception:
            # Return an error status if the token is not found
            return JsonResponse({"status": 400})
        # Verify if the provided token is valid
        if not verify_token(token):
            return JsonResponse({"status": 400, "errors": "invalid token"})
        # Extract token information
        data = extrat_token_info(token)
        u_id = data["id"]
        # Load the JSON body from the request
        body = json.loads(request.body)

        # Get the question being voted on and save the vote
        temp_question = Question.objects.get(id=body['id'])
        v = Vote(user_id=u_id, is_approved=body['accepted'], justification=body['value'], question_id=body['id'])
        v.save()

        # Check and handle if the question has been approved by 3 votes
        if Vote.objects.filter(question__id=body['id'], is_approved=True).count() == 3:
            temp_question.state = 4
            temp_question.save()
            creator = User.objects.get(id=temp_question.user.id)

            # Promote the user if they have 3 approved questions
            if Question.objects.filter(user__id=creator.id, state = 4).count() == 3:
                creator.role = 2
                creator.save()
            return JsonResponse({"status": 200, "message": f"question {body['id']} has been approved"})

        # Check and handle if the question has been rejected by 3 votes
        if Vote.objects.filter(question__id=body['id'], is_approved=False).count() == 3:
            temp_question.state = 3
            temp_question.save()
            return JsonResponse({"status": 200, "message": f"question {body['id']} has been rejected"})

        # Default return for successful vote submission
        return JsonResponse({"status": 200, "message": "vote has been saved"})

