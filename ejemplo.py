def manejar_archivo(nombre_archivo, modo, contenido=None):
    if modo not in ['r', 'w', 'a', 'x']:
        raise IOError("Modo no soportado. Usa 'r', 'w', 'a' o 'x'.")
    try:
        with open(nombre_archivo, modo) as archivo:
            if modo == 'r':
                return archivo.read()
            else:
                archivo.write(contenido)
                return f"Contenido escrito en {nombre_archivo} en modo {modo}"
    except FileNotFoundError:
        return f"El archivo {nombre_archivo} no existe y no puede ser leído."
   
print(manejar_archivo("contraseña.txt", "w", "P@sw0rd123"))
print(manejar_archivo("contraseña.txt", "r"))