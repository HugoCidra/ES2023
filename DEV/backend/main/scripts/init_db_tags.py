from api.models import *


def run():
    tags = [
        "ES",
        "AC",
        "BD",
        "COMP",
        "IPRP",
        "POO",
        "PPP",
        "RC",
        "SI",
        "SO",
        "TC",
        "TI",
    ]
    for tag in tags:
        new_tag = Tag(value=tag)
        new_tag.save()
