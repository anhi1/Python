# Haz una función para separar una frase en una lista de palabras

def separar_una_frase(frase:str) -> list:
    palabras = frase.split()
    return palabras

una_frase = input("dime una frase: ")
lista_palabras = separar_una_frase(una_frase)
print("lista de palabras", lista_palabras)






