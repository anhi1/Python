# convertir de numero romano a decimal

def romano_a_decimal(romano:str) -> int:
    valores = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    decimal = 0
    prev_value = 0

    for char in romano:
        value = valores[char]
        if value < prev_value:
            decimal -= value
        else:
            decimal += value
        prev_value = value
    return decimal 

romano = input("introduce un nuemro romano: ")
decimal = romano_a_decimal(romano)
print(f"el numero decimal es: {decimal}")
