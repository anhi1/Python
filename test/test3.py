# TEST DRIVEN DEVELOPMENT TDD
# el test Driven dvelopment es una practica que consiste en hacer antes el test del codigo, para despues ir haciendo el codigo de acuerdo a los test. Esta metodologia se llama Red-Green-refactor
# pip install pytest | pytest test3.py
import pytest
from prueba import Pato

instancia = Pato()
def test_pato():
    assert instancia.quack() == "quack!"

