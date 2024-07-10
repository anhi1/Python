""" 
Un decorador es un closure que devuelve como return una funcion arbitraria, de
forma que complementa (o decora) otra funcion
"""

import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {round(fin - inicio, 3)} segundos")
        return resultado
    return wrapper

@medir_tiempo
def suma(a, b):
    time.sleep(2)
    return a + b

resultado = suma(3, 4)
print(f"Resultado: {resultado}")

# Decorador de En proceso
def process_decorator(func):
    def wrapper(*args, **kwargs):
        print("En proceso ...")
        return func(*args, **kwargs)
    return wrapper

@process_decorator
def suma(a, b):
    time.sleep(2)
    return a + b

resultado = suma(3, 4)

def decorador_con_args(arg1, arg2):
    return decorador

@decorador_con_args("Hola", "Mundo")
def funcion_ejemplo():
    print("Función ejecutada")

funcion_ejemplo()