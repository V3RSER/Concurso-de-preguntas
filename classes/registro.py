import datetime

class Registro:

    def __init__(self,  jugador, condicion):
        self.jugador = jugador
        self.condicion = condicion
        self.fecha = datetime.datetime.today()
        self.dinero_ganado = jugador.obtener_dinero()
        self.premios_ganados = jugador.obtener_premios()

    def obtener_dinero_ganado(self):
        return self.dinero_ganado

    def obtener_contenido(self):
        return f"Tipo: {self.condicion}\nFecha: {self.fecha}\nDinero ganado: {self.dinero_ganado}"