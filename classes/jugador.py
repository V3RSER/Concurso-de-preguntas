from classes.registro import Registro

class Jugador:

    def __init__(self, nombre):
        self.nombre = nombre
        self.registros = []
        self.premios = []
        self.dinero = 0
        self.billetera = 0

    def generar_registro(self, condicion):
        if (condicion == 'victoria') | (condicion == 'retirado'):
            self.billetera += self.dinero
        else:
            self.premios = []
            self.dinero = 0
        self.registros.append(Registro(self, condicion))

    def elminiar_registro(self, registro):
        self.registros.remove(registro)

    def obtener_premios(self):
        return self.premios

    def establecer_dinero(self, dinero):
        self.dinero = dinero


    def agregar_premio(self, premio):
        self.premios.append(premio)
        self.dinero += premio.obtener_dinero()

    def obtener_dinero(self):
        return self.dinero

    def obtener_nombre(self):
        return self.nombre

    def obtener_billetera(self):
        return self.billetera

    def obtener_registros(self):
        return self.registros