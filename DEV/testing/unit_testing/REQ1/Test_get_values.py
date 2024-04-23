from api.REQ1 import views

def test_get_values():
   
    payload = {'a': '1', 'b': '2'}

    existent_key = ['a']
    non_existent_key = ['c']

    existent_keys = ['a', 'b']
    mixed_keys = ['a', 'c']
    non_existent_keys = ['c', 'd']

    #primeiro caso: uma chave e a chave existe
    res = views.get_values(payload, existent_key)
    try:
        assert next(res) == '1'
    except StopIteration:
        pass

    #segundo caso: uma chave e a chave não existe
    res = views.get_values(payload, non_existent_key)
    try:
        assert next(res) is None
    except StopIteration:
        pass
    
    #terceiro caso: varias chaves e existem todas
    res = views.get_values(payload, existent_keys)
    assert next(res) == '1'
    assert next(res) == '2'

    #quarto caso: varias chaves e só existem algumas
    res = views.get_values(payload, mixed_keys)
    assert next(res) == '1'
    assert next(res) is None

    #quinto caso: varias chaves e nao existe nenhuma
    res = views.get_values(payload, non_existent_keys)
    assert next(res) is None
    assert next(res) is None