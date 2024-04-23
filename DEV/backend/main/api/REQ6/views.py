from cgi import test
from itertools import count
from urllib import response
import json
from ..utils.tokens import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..models import *
import random
from django.views.decorators.http import require_http_methods


# Define a view function named 'test' to handle a POST request
def create_test(request):
    # Extract the token from the request
    token = extract_token(request)
    # Verify the extracted token
    if not verify_token(token):
        print(extrat_token_info(token))
        return JsonResponse({"status": 400, "errors": "invalid token"})

    # Extract user ID from the token information
    u_id = extrat_token_info(token)["id"]
    # Loads the body from the request
    data = json.loads(request.body)

    t_list = data["tags"]

    c = 20

    # tag1 = list(Question.objects.filter(tag__value=t_list[0]).exclude(num_tests__gt=1).filter(state=4))
    # tag2 = list(Question.objects.filter(tag__value=t_list[1]).exclude(num_tests__gt=1).filter(state=4))

    # print("\n\n\n\nDEBUG\n\n\n\n")
    # tag1_id = Tag.objects.all().filter(value=t_list[0])[0].id
    # tag2_id = Tag.objects.all().filter(value=t_list[1])[0].id

    tags_query = Tag.objects.all().filter(value=t_list[0])
    if tags_query.exists():
        tag1_id = tags_query[0].id
    else:
        return JsonResponse({"status": 400, "errors": "Tag not found"})

    tags_query = Tag.objects.all().filter(value=t_list[0])
    if tags_query.exists():
        tag2_id = tags_query[0].id
    else:
        return JsonResponse({"status": 400, "errors": "Tag not found"})

    tags_query = Question.tags.through.objects.all().filter(tag_id=tag1_id)
    q_ids_tag1 = [q.question_id for q in tags_query]

    tags_query = (
        Question.tags.through.objects.all()
        .filter(tag_id=tag2_id)
        .exclude(question_id__in=q_ids_tag1)
    )
    q_ids_tag2 = [q.question_id for q in tags_query]

    tag1 = list(
        Question.objects.filter(id__in=q_ids_tag1)
        .exclude(num_tests__gt=1)
        .filter(state=4)
    )
    tag2 = list(
        Question.objects.filter(id__in=q_ids_tag2)
        .exclude(num_tests__gt=1)
        .filter(state=4)
    )

    # print("\n\n\n\nDEBUG\n\n\n\n")
    # print(q_ids_tag1)
    # print(q_ids_tag2)
    # print(t_list[0])
    # print(t_list[1])
    # print(tag1_id)
    # print(tag2_id)

    # Ensure that the retrieved question lists don't exceed 10 items each
    if len(tag1) > 10:
        tag1 = random.sample(tag1, 10)
    if len(tag2) > 10:
        tag2 = random.sample(tag2, 10)

    # Check if both tag lists are empty
    if len(tag1) == 0 and len(tag2) == 0:
        return JsonResponse({"status": 400, "errors": "No questions available."})

    # Calculate remaining question count
    c = c - len(tag1) - len(tag2)

    # If more questions are needed, fetch them from the database
    if c > 0:
        # temp3 = Question.objects.exclude(num_tests__gt=1).filter(state=4).exclude(tag__value=t_list[0]).exclude(tag__value=t_list[1])[:c]
        temp3 = (
            Question.objects.exclude(num_tests__gt=1)
            .filter(state=4)
            .exclude(id__in=q_ids_tag1)
            .exclude(id__in=q_ids_tag2)[:c]
        )
        tag2.extend(list(temp3))

    # Combine the question lists
    q_list = tag1 + tag2

    # Check if there are enough questions for a test
    if len(q_list) < 20:
        return JsonResponse(
            {"status": 400, "errors": "Not enough quizzes to make a test."}
        )

    # Count the occurrence of tags in the selected questions
    tag_count = {}
    for q in q_list:
        # query the tag values of the question

        tag_ids = [
            t_id.tag_id
            for t_id in Question.tags.through.objects.all().filter(question_id=q.id)
        ]
        # print(tag_ids)
        # print("\n\n\n\nDEBUG\n\n\n\n")
        for t_id in tag_ids:
            try:
                tag_count[Tag.objects.get(id=t_id).value] += 1
            except KeyError:
                tag_count[Tag.objects.get(id=t_id).value] = 1

    # Get the user and create a new test
    user = User.objects.get(id=u_id)
    v = Test(title=data["title"], creator=user)
    v.save()
    v.questions.add(*q_list)

    # Update the 'num_tests' field for each question
    for q in q_list:
        q.num_tests += 1
        q.save()

    # Add tags to the test
    v.tags.add(Tag.objects.get(value=data["tags"][0]))
    v.tags.add(Tag.objects.get(value=data["tags"][1]))

    return JsonResponse(
        {"status": 200, "message": "Test created successfully", "count": tag_count}
    )


# Define a view function named 'tags' to handle a GET request
@require_http_methods(["GET"])
def tags(request):
    # Extract the token from the request
    token = extract_token(request)
    # Verify the extracted token
    if not verify_token(token):
        print(extrat_token_info(token))
        return JsonResponse({"status": 400, "errors": "invalid token"})

    # Retrieve a list of tag values from the database
    tags = list(Tag.objects.all().values_list("value", flat=True))
    # Return the list of tags as a JSON response
    return JsonResponse({"status": 200, "tags": tags})
