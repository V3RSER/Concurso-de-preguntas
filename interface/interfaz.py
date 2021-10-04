import tkinter as tk

from interface.ventana_editor import VentanaEditor
from interface.ventana_inicio import VentanaInicio
from interface.ventana_ronda import VentanaRonda

class Interfaz:

    def __init__(self, concurso):
        self.concurso = concurso
        #self.crear_ventana_inicio()
        self.crear_ventana_editor()

    def crear_ventana_inicio(self):
        self.ventana_inicio = VentanaInicio(self.concurso, self)

    def crear_ventana_ronda(self):
        self.ventana_ronda = VentanaRonda(self.concurso, self)

    def crear_ventana_editor(self):
        rondas = self.concurso.obtener_rondas()
        self.ventana_editor = VentanaEditor(
            [rondas[0].obtener_categoria(), rondas[1].obtener_categoria(),
             rondas[2].obtener_categoria(), rondas[3].obtener_categoria(),
             rondas[4].obtener_categoria()], self)
