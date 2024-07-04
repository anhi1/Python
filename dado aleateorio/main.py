from interfaz import INTERFAZ, INTERFAZ_FINAL
from dado import Dado

print(INTERFAZ)

numero_caras = int(input("De cuantas caras quieres el dado: "))
dado = Dado(numero_caras)
tiradas = []
terminar = False

while terminar is False:
    tirada = dado.tirada()
    tiradas.append(tirada)
    if input(INTERFAZ_FINAL).lower() not in ("si", "yes", "y"):
        terminar = True

print(tiradas)
