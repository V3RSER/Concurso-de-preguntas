class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.premios = []
        self.billetera = 0

    def agregar_premio(self, premio):
        self.premios.append(premio)
        self.billetera += premio.obtener_dinero()

    def obtener_billetera(self):
        return self.billetera

class RanuraGuardado():
    pass
