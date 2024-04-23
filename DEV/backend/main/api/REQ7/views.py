from django.http import HttpRequest, JsonResponse, HttpResponse
from typing import List, TextIO
from ..models import Question, Tag, Option, User
from ..utils import tokens

from pprint import pprint
import xmltodict

def is_true(value: str) -> bool:
    """converts a string to a boolean

    Args:
        value (str): string to convert

    Returns:
        bool: True if string is "True" or "true" or "1", False otherwise
    """
    if value == "True" or value == "true" or value == "1":
        return True
    return False

def load_info(request: HttpRequest):
    """View to load a xml file

    Args:
        request (HttpRequest): request

    Returns:
        _type_: Json response
    """
    
    # check if method is POST (create)
    if request.method != "POST":
        return JsonResponse({'status': 405, 'log': f"Method ({request.method}) not alowed, only POST"})

    # check user auth
    token = tokens.extract_token(request)
    if token is None:
        return JsonResponse({'status': 500, 'log': "User not loged in"})


    # check token validation
    token_info = tokens.extrat_token_info(token)
    if token_info is None:
        # if not tokens.verify_token(token):
        return JsonResponse({'status': 500, 'log': "Expired session"})
    

    # parsing do ficheiro
    file: TextIO = request.FILES['file']
    try:
        obj = xmltodict.parse(file.read().replace(b"A&D", b"AD"))
    except Exception as e:
        file.close()
        return JsonResponse({'status': 505, 'log': str(e)})
    file.close()

    # check for format of xml in perguntas part
    try:
        perguntas = obj['quizzess']['perguntas']['pergunta']
    except Exception:
        return JsonResponse({'status': 505, 'log': 'wrong format in perguntas'})
    del obj
    
    # get user to associate
    user = User.objects.get(id=token_info['id'])
    
    # if there is just one pergunta it saves as a dict and not list (need to transform)
    if type(perguntas) == dict:
        perguntas = [perguntas]
    
    #verifica se as perguntas têm opcoes repetidas
    string_report = ''
    for pergunta in perguntas:
        if pergunta['respostas'] is None or len(pergunta['respostas']['resposta']) != 6:
            string_report += f"Question with wrong number of options -\n"
            string_report += f"Question - {pergunta['descricao']}\n"
            string_report += "\n"
            return JsonResponse({'status': 505, 'log': 'Question with wrong number of options'})
        else:
            for i in range(len(pergunta['respostas']['resposta'])):
                for j in range(i+1, len(pergunta['respostas']['resposta'])):
                    if pergunta['respostas']['resposta'][i]['designacao'] == pergunta['respostas']['resposta'][j]['designacao']:
                        string_report += f"Repeated Option in a Question in XML -\n"
                        string_report += f"Question - {pergunta['descricao']}\n"
                        string_report += f"Option - {pergunta['respostas']['resposta'][i]['designacao']}\n"
                        string_report += "\n"
                        return JsonResponse({'status': 505, 'log': 'Repeated Option in a Question in XML'})

    #if string_report != '':
    #    print(string_report)
    #    return JsonResponse({'status': 505, 'log': string_report})

    # verifica se a perguntas repetidas no XML
    for pergunta_id in range(len(perguntas)):
        for i in range(pergunta_id+1, len(perguntas)):
            if perguntas[pergunta_id]['descricao'] == perguntas[i]['descricao']:
                # verifica se opcoes repetidas
                controlo = 0
                for j in range(len(perguntas[pergunta_id]['respostas']['resposta'])):
                    for k in range(j, len(perguntas[i]['respostas']['resposta'])):
                        if perguntas[pergunta_id]['respostas']['resposta'][j]['designacao'] == perguntas[i]['respostas']['resposta'][k]['designacao']:
                            print(f"-> {perguntas[pergunta_id]['respostas']['resposta'][j]['designacao']} == {perguntas[i]['respostas']['resposta'][k]['designacao']}")
                            controlo += 1
                
                if controlo >= len(perguntas[pergunta_id]['respostas']['resposta']):
                    string_report += f"Repeated Question in XML -\n"
                    string_report += f"Question - {perguntas[pergunta_id]['descricao']}\n"
                    for j in perguntas[pergunta_id]['respostas']['resposta']:
                        string_report += f"Option - {j['designacao']}\n"
                    string_report += "\n"
                    return JsonResponse({'status': 505, 'log': 'Repeated Question in XML'})
    
    #if string_report != '':
    #    print(string_report)
    #    return JsonResponse({'status': 505, 'log': string_report})

    #for i in perguntas:
    #    print(i, end="\n\n")
    contador = 0
    for pergunta in perguntas:
        # verifica se a pergunta ja existe
        contador += 1
        if Question.objects.filter(body=pergunta['descricao']).exists():
            quizes = Question.objects.filter(body=pergunta['descricao'])
            for quiz in quizes:
                options = Option.objects.filter(question=quiz)
                count = 0
                for option in options:
                    controlo = 1
                    for i in range(len(pergunta['respostas']['resposta'])):
                        option_test = pergunta['respostas']['resposta'][i]['designacao']
                        if option.body == option_test and option.is_correct == is_true(pergunta['respostas']['resposta'][i]['valor_logico']):
                            count += 1
                            controlo = 0
                    if controlo == 1:
                        break

                if count == 6:
                    string_report += f"Question already exists -\n"
                    string_report += f"{quiz.body}\n"
                    for i in options:
                        string_report += f"{i.body} - logical value {i.is_correct}\n"
                    string_report += "\n"
                    return JsonResponse({'status': 505, 'log': f'Question {contador} already exists'})

        
    #if string_report != '':
    #    print(string_report)
    #    return JsonResponse({'status': 505, 'log': string_report})


    for pergunta in perguntas:
        # criar a pergunta
        temp_question = Question(user=user, body=pergunta['descricao'], state=2)

        # check for format of xml in tags part
        try:
            temp_tag_list = pergunta['tags']['tag']
        except Exception:
            return JsonResponse({'status': 505, 'log': 'wrong format in tags'})

        # if there is just one tag it saves as a string and not list (need to transform)
        if type(temp_tag_list) == str:
            temp_tag_list = [temp_tag_list]

        temp_question.save()

        # associar as tags
        for tag in temp_tag_list:
            try:
                temp_tag = Tag.objects.get(value=tag)
            except Tag.DoesNotExist:
                # if it doesnt find tag creats it

                temp_tag = Tag(value=tag)
                temp_tag.save()
            
            # temp_question.tag = temp_tag
            temp_question.tags.add(temp_tag)
        

        # criar as respostas
        if pergunta['respostas'] is None:
            continue

        temp_opts_list = pergunta['respostas']['resposta']
        if type(temp_opts_list) == dict:
            temp_opts_list = [temp_opts_list]
        
        # print(type(temp_opts_list['resposta']))
        for resp in temp_opts_list:
            if resp['justificacao'] is None:
                resp['justificacao'] = ""
            
            temp_resp = Option(
                question=temp_question,
                body=resp['designacao'],
                is_correct= resp['valor_logico'] == "True",
                justification= resp['justificacao']
            )
            temp_resp.save()

    return JsonResponse({"status": 200})


def send_info(request: HttpRequest):
    """view to send questions in xml format

    Args:
        request (HttpRequest): request

    Returns:
        _type_: HttpResponse with file
    """


    # check if method is GET
    if request.method != "GET":
        return JsonResponse({'status': 405, 'log': f"Method ({request.method}) not alowed, only GET"})

    # check user auth
    token = tokens.extract_token(request)
    if token is None:
        return JsonResponse({'status': 500, 'log': "User not loged in"})


    # check token validation
    if not tokens.verify_token(token):
        return JsonResponse({'status': 500, 'log': "Expired session"})

    # get 'json' format of questions    
    perguntas = []
    questoes = Question.objects.exclude(state=1).exclude(state=3).all().filter(user=User.objects.get(id=tokens.extrat_token_info(token)['id']))

    print(questoes.exists())
    if not questoes.exists():
        print("no questions")
        return JsonResponse({'status': 505, 'log': "You have no questions to export"})

    for i in questoes:
        
        #respostas
        temp_resposta = []
        for j in i.option_set.all():
            temp_resposta.append({
                'designacao': j.body,
                'justificacao': j.justification,
                'valor_logico': str(j.is_correct)
            })

        print([tag.value for tag in i.tags.all()])

        temp_pergunta = {
            'descricao': i.body,
            'tags': {'tag': [tag.value for tag in i.tags.all()]},  # so uma tag obrigatoria
            'respostas': {'resposta': temp_resposta}
        }
        
        # check if this question is equal to other
        if any(temp_pergunta == j for j in perguntas):
            print("repetida")
            continue

        perguntas.append(temp_pergunta)
    
    print("DEBUG:")
    print(perguntas)

        # total dict
    resp = {'quizzess': {
            '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            'perguntas': {'pergunta': perguntas}
        }}

    # transform dict in to xml
    temp = xmltodict.unparse(
        resp,
        pretty=True,  # to format with tabs and enters
        newl='\r\n'  # CRLF format
    ).replace("<tag>AD</tag>", "<tag>A&D</tag>")
        
    response = JsonResponse({'status':200, 'data':temp})
    response['Content-Disposition'] = 'attachmen'
    return response


def temp(request: HttpRequest):
    with open("temp.xml", "r") as file:
        obj = xmltodict.parse(file.read())

    perguntas = obj['quizzess']['perguntas']['pergunta']
    del obj
    
    pprint(perguntas)

    # domtree: xml.dom.minidom.Document = xml.dom.minidom.parse("temp.xml")
    # group: xml.dom.minidom.Element = domtree.documentElement
    
    # quizzes: List[xml.dom.minidom.Element] = group.getElementsByTagName("pergunta") #[0].getElementsByTagName("pergunta")

    # pprint(quizzes)
    # for i in quizzes:
    #     print(i.getElementsByTagName("descricao")[0].nodeValue)
    #     print(i.childNodes[0].nodeValue)
    #     # print(type(i))
    # obj = untangle.parse(resource)
    # print(obj)
    return JsonResponse({})
