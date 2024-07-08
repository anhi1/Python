# PITEST
# primero el entonro virtual: python -m venv .env  | .\.env\Scripts\activate | pip install pytest | pytest test2.py
# En la prueba tecnica usar pytest


def suma(a: int | float, b: int | float) -> int | float:
    return a + b

import pytest

def test_suma_positivos():
    assert suma(2,3) == 5

def test_suma_negativos():
    assert suma(-1, 1) == 0




