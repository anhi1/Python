# GENERADOR DE PELOTAS

# hacer un generador para repetir pelotas
# pelotas --> radio (constante) y color (se pide al usuario)

# class Pelota:
#     def __init__(self, radio: int, color: str):
#         self.radio = radio
#         self.color = color

# def generadorPelota(pelotas_a_crear: int):
#     for _ in range(pelotas_a_crear):
#         radio = int(input("Ingrese el radio de la pelota: "))
#         color = input("Ingrese el color de la pelota: ")
#         yield Pelota(radio, color)

# for pelota in generadorPelota(2):
#     print(f"Pelota con radio {pelota.radio} y color {pelota.color}")



# 2 FORMA DE GENERAR PELOTAS
class Pelota:
    def __init__(self, radio, color):
        self.radio = radio
        self.color = color

    def __str__(self):
        return f"pelota de color {self.color} con radio {self.radio}"

def generadorPelotas():
    while True:
        color = input("ingrese el color de la pelota")
        yield Pelota(radio, color)
        continuar = input("desea genrar otra pelota")
        if continuar.lower() != 's':
            break

pelotas = []
for pelota in generator_pelotas():
    print(pelota.color, print(pelota.radio))
    pelotas.append(pelota)