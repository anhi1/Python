""" 
Un closure es una función anidada que recuerda los valores de las variables del
entorno en el que fue creada, incluso después de que ese entorno haya terminado
su ejecución. Es una característica de los lenguajes de programación que soportan
funciones de primera clase, como Python o Javascript.
"""

def exterior(mensaje):
    # Una forma
    def interior():
        print(mensaje)
        
    # Otra forma
    interior = lambda: print(mensaje)
    return interior

mi_closure = exterior("¡Hola, mundo!")
mi_closure()

def calculadora(valor1: int, operacion: str, valor2: int):
    if operacion == "+":
        calculo = lambda: valor1 + valor2
    elif operacion == "-":
        calculo = lambda: valor1 - valor2
    elif operacion == "*":
        calculo = lambda: valor1 * valor2
    elif operacion == "/":
        try:
            calculo = lambda: valor1 / valor2
        except ZeroDivisionError:
            print("No puedes dividir por 0")
            calculo = None
    else:
        raise ValueError()
    try:
        print(f"{calculo() if calculo else "No hay resultado"}")
    except Exception as e:
        print(str(e))  # Solo por si hay otros errores raros
    return calculo
 
calc = calculadora(10, "/", 2)
calc()
