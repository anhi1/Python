# 1 convertir de numero romano a decimal

# def romano_a_decimal(romano:str) -> int:
#     valores = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
#     suma_total = 0
#     valor_anterior = 0

#     for simbolo in romano:
#         valor_actual = valores[simbolo]
#         if valor_actual > valor_anterior:
#             suma_total += valor_actual - 2 * valor_anterior
#         else:
#             suma_total += valor_actual
#         valor_anterior = valor_actual
#     return suma_total 

# numero_romano = input("introduce un numero romano: ")
# numero_decimal = romano_a_decimal(numero_romano)
# print(f"el numero decimal es: {numero_decimal}")


# 2 convertir de numero romano a decimal

def romano_a_decimal(romano:str) -> int:
    valores = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total = 0
    previo = 0

    for simbolo in reversed(romano): 
        valor = valores[simbolo]
        if valor < previo:
            total -= valor 
        else: 
            total += valor
        previo = valor
    return total
    
numero_romano = input("Introduce un número romano: ")
numero_decimal = romano_a_decimal(numero_romano)
print(f"El número decimal de '{numero_romano}' es: {numero_decimal}")