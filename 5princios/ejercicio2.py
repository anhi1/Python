class Bombilla:
    def on(self):
        print("Se ha encendido")

    def off(self):
        print("Se ha apagado")

class Interruptor:
    def __init__(self, bombilla: Bombilla):
        self.bombilla = bombilla
        self.status = False  # La bombilla empieza apagada

    def on_off(self):
        if self.status:
            self.bombilla.off()
        else:
            self.bombilla.on()