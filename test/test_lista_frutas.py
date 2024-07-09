import pytest
from lista_frutas import ListaFrutas

def test_añadir_fruta():
    instancia = ListaFrutas()
    fruta = "manzana"
    instancia.añadir_fruta(fruta)
    assert instancia.lista[0] == fruta
    with pytest.raises(TypeError, match="Eso no es una fruta"):
        instancia.añadir_fruta(100)