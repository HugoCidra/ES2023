from django.http import JsonResponse, HttpRequest
from ..models import User, Question, SolvedTest
from django.db.models import Count, Sum
from ..utils.tokens import verify_token, extrat_token_info, extract_token

invalid_token = "could not extract token info."
wrong_request = "wrong request type."


def unfinished_reproved_quizzes(request: HttpRequest):
    """returns all quizzes that belong to the user

    Args:
        request (HttpRequest): request

    Returns:
        _type_: None
    """
    if request.method != "GET":
        return {"status": 404, "message": wrong_request}

    # Check if the user is logged

    token = extract_token(request)

    if not verify_token(token):
        return JsonResponse({"error": {"code": 400, "message": invalid_token}})

    user_info = extrat_token_info(token)
    user_id = user_info.get("id")

    response = list(
        Question.objects.filter(user__id=user_id).values_list(
            "id", "state", "body"
        )
    )

    return JsonResponse({"status": 200, "unfinished_reproved_quizzes": response})


def solvers(request: HttpRequest):
    """return all quiz solvers

    Args:
        request (HttpRequest): request

    Returns:
        _type_: None
    """
    if request.method != "GET":
        return {"status": 404, "message": wrong_request}

    # Check if the user is logged
    token = extract_token(request)

    if (verify_token(token)) == False:
        return JsonResponse({"error": {"code": 400, "message": invalid_token}})

    solvers = list(
        SolvedTest.objects.values_list("user__name")
        .annotate(score=Sum("grade"))
        .order_by("-score")
    )

    return JsonResponse({"status": 200, "solvers": solvers})


def creators(request: HttpRequest):
    """return all quiz creators

    Args:
        request (HttpRequest): request

    Returns:
        _type_: None
    """
    if request.method != "GET":
        return {"status": 404, "message": wrong_request}

    # Check if the user is logged

    token = extract_token(request)

    if (verify_token(token)) == False:
        return JsonResponse({"error": {"code": 400, "message": invalid_token}})

    creators = list(
        Question.objects.filter(state=4)
        .values_list("user__name")
        .annotate(score=Count("user"))
        .order_by("-score")
    )

    return JsonResponse({"status": 200, "creators": creators})


def is_solver(request: HttpRequest):
    """checks if the user is a solver

    Args:
        request: request

    Returns:
        _type_: None
    """
    if request.method != "GET":
        return {"status": 404, "message": wrong_request}

    # Check if the user is logged in

    token = extract_token(request)

    if (verify_token(token)) == False:
        return JsonResponse({"error": {"code": 400, "message": invalid_token}})

    user_info = extrat_token_info(token)
    user_id = user_info.get("id")

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"status": 400, "response": "could not find the user"})

    response = user.role == 2

    return JsonResponse({"status": 200, "response": response})
