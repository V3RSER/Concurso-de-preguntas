import tkinter as tk
from interface.ventana_inicio import VentanaInicio
from interface.ventana_ronda import VentanaRonda

class Interfaz:

    def __init__(self, concurso):
        self.concurso = concurso
        self.crear_ventana_inicio()

    def crear_ventana_inicio(self):
        self.ventana_inicio = VentanaInicio(self.concurso, self)

    def crear_ventana_ronda(self):
        self.ventana_ronda = VentanaRonda(self.concurso, self)
