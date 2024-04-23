# View manual

## load_info
- path: `api/REQ7/load_info/`
- method: POST
- user auth: True
- description: loads a xml file with questions and respective answers.

### Request format
```
{
    ...
    "headers": {
        ...
        "content-type": "multipart/form-data"
    },
    "file" : <input type="file" : name="file">,
    "token": <str: token>   
}
```
FILES will only contain data if the request method was POST and the form that posted to the request had enctype="multipart/form-data". Otherwise, FILES will be a blank dictionary-like object.

### Response format
If succeded:
```
{
    "status": 200
}
```

### Status codes
- 405 -> invalid method
- 500 -> invalid authentication
- 505 -> invalid file 
- 200 -> success

---
## send_info
- path: `api/REQ7/send_info/`
- method: GET
- user auth: True
- description: send questions in xml format

### Request format
```
{ }
```

### Response format
```
{
    "status": 200, 
    "data":temp  
}
```
temp is an xml conversion of a dictionary(perguntas) with all the  questions:
```
"perguntas":
[{
        "descricao":<str body>,
        "tags":{<str tag>,...},
        "respostas":[{
                                "designacao": <str designacao>,
                                "justificacao": <str justificacao>,
                                "valor_logico": <str valor_logico>
                    },...]
                    
},...]
```
### Status codes
- 405 -> invalid method
- 500 -> invalid authentication
- 200 -> success

---
## temp 
Not done.

