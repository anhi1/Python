def calculadora(a: int, b: int, operacion: str):
    if operacion == "+":
        calculo = lambda: a + b
    elif operacion == "-":
        calculo = lambda: a - b
    elif operacion == "*":
        calculo = lambda: a * b
    elif operacion == "/":
        try: 
            calculo = lambda: a / b
        except ZeroDivisionError:
            print("no puedes dividir por cero")
    def suma():
        print(a + b)
        return suma

mi_clousure = calculadora(5, 3)
mi_clousure()
    
    