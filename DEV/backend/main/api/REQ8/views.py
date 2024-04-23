from django.http import HttpRequest, JsonResponse
from django.db.utils import IntegrityError

from ..models import User, Test, Question, Option, SolvedTest
from ..utils import tokens, requests


def get_username(request):

    """ 
        Returns the username
       
        Args:
            request(HttpRequest): request
        
        Returns:
            JsonResponse: HttpResponse with the username in JSON format
    """

    if request.method != 'GET':
        return {"status": 400, "message": "wrong_request"}

    # Check if the user is logged in
    token = tokens.extract_token(request)

    if (token == None or tokens.verify_token(token) == False):
        return JsonResponse({"error": {"code": 400, "message": "invalid_token: User is not logged in"}})

    # Get the User from the token
    user_info = tokens.extrat_token_info(token)

    try:
        user = User.objects.get(pk=user_info.get("id"))
    except User.DoesNotExist:
        return JsonResponse({'status': 400, 'response': "could not find the user"})

    # Return the username
    return JsonResponse({"status":200 ,"username": user.name})




def get_stats_solver(request):

    """ 
        Function to get the stats of a user
       
        Args:
            request(HttpRequest): request  
        
        Returns:
            JsonResponse: HttpResponse with the data information in JSON format
            data is a list which each index is a tuple with the name of the SolvedTest and the score :
                    [(name1, score1),(name2, score2),...]
    """

    if request.method != 'GET':
        return {"status": 400, "message": "wrong_request"}

    # Check if the user is logged in
    token = tokens.extract_token(request)

    if (token == None or tokens.verify_token(token) == False):
        return JsonResponse({"error": {"code": 400, "message": "invalid_token: User is not logged in"}})

    # Check if user is Solver
    user_info = tokens.extrat_token_info(token)
    user_id = user_info.get("id")

    try:
        user = User.objects.get(pk=user_info.get("id"))
    except User.DoesNotExist:
        return JsonResponse({'status': 400, 'response': "could not find the user"})

    if user.role != 2:
        return JsonResponse({"status":401, 'response': "user is not solver"})


    stests=SolvedTest.objects.filter(user=user)

    resposta={}

    for stest in stests:
        for opt in stest.options.all():
            # tag_name=opt.question.tag.value

            tag_names = opt.question.tags.all()
            tag_names = [ t_n.value for t_n in tag_names ]
            
            for tag_name in tag_names:
                if tag_name not in resposta:
                    resposta[tag_name]=[0,0]
                
                if opt.is_correct:
                    resposta[tag_name][0]+=1
                else:
                    resposta[tag_name][1]+=1
        
    
    data=[]
    for i in resposta:
        data.append({
            "name":i,
            "x":resposta[i][0],
            "y":resposta[i][1],
        })


    #devolução da: uniquetag:[TAG1,TAG2,....]  percenta_aceite:[[%aceite_TAG1,%rejeitadoTAG1],[%aceite_TAG2,%rejeitadoTAG2],...]
    return JsonResponse({'status': 200, "data":data})



def get_tags_creator(request):

    """ 

        Nao faco ideia do que se passa aqui
       
        Args:
            request(HttpRequest): request
        
        Returns:
            JsonResponse: HttpResponse with the uniquetag:[TAG1,TAG2,....]  percenta_aceite:[[%aceite_TAG1,%rejeitadoTAG1],[%aceite_TAG2,%rejeitadoTAG2],...] in JSON format
    """

    if request.method != 'GET':
        return {"status": 400, "message": "wrong_request"}

    # Check if the user is logged in
    token = tokens.extract_token(request)
    if (token == None or tokens.verify_token(token) == False):
        return JsonResponse({"error": {"code": 400, "message": "invalid_token: User is not logged in"}})

    # Check if user is a creator
    user_info = tokens.extrat_token_info(token)


    try:
        user1 = User.objects.get(pk=user_info.get("id"))
    except User.DoesNotExist:
        return JsonResponse({'status': 400, 'response': "could not find the user"})

    
 
    unique_tags=[]
    rescerta_reserrada=[]
    question = Question.objects.filter(user=user1)
    resposta={}
    #tirar informação necessária
    for squestion in question:
        if squestion.state not in (3,4):
            continue
        # tag_name=squestion.tag.value
        tag_names = squestion.tags.all()
        tag_names = [ t_n.value for t_n in tag_names ]
        
        for tag_name in tag_names:
            if tag_name not in resposta:
                resposta[tag_name]=[0,0]
            
            if squestion.state== 3:
                resposta[tag_name][1]+=1
            if squestion.state== 4:
                resposta[tag_name][0]+=1
        

    #serve para colocar informação em 2 arrays(unique_tag e percentaaceite) vai colocar nas mesmas posições dos arrays, a tag única e a percentagem de quizzes criados com a tag aceites
    data=[]
    for i in resposta:
        data.append({
            "name":i,
            "x":resposta[i][0],
            "y":resposta[i][1],
        })

    #devolução da: uniquetag:[TAG1,TAG2,....]  percenta_aceite:[[%aceite_TAG1,%rejeitadoTAG1],[%aceite_TAG2,%rejeitadoTAG2],...]
    return JsonResponse({'status': 200, "data":data})
