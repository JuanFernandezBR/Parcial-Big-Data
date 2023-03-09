import pytest
from unittest.mock import Mock
from extraer import extraer
import json

def test(mock):
    
    mock_info = mock.patch('extraer.extraer')
    mock_info.return_value = '{"hits":{"hits":""}}'
    
    cantidad = 3
    resultado = extraer(cantidad)
    res_dic = json.loads(resultado)
    
    assert isinstance(resultado, str)
    assert resultado[0] == '{'
    assert "hits" in res_dic.keys()
    assert len(res_dic["hits"]["hits"]) >= cantidad