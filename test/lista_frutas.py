class ListaFrutas:
    def __init__(self):
        self.lista = []

    def añadir_fruta(self, fruta: str):
        if isinstance(fruta, str):
            self.lista.append(fruta)
        else:
            raise TypeError("Eso no es una fruta")