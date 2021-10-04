import pickle
import tkinter as tk

from interface.ventana_editor import VentanaEditor
from interface.ventana_inicio import VentanaInicio
from interface.ventana_ronda import VentanaRonda
from interface.ventana_registro import VentanaRegistro

class Interfaz:

    def __init__(self, concurso, jugadores):
        self.concurso = concurso
        self.jugadores = jugadores
        self.crear_ventana_inicio()

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

    def crear_ventana_registro(self):
        self.ventana_registro = VentanaRegistro(self.jugadores, self)

    def guardar_jugadores(self):
        with open('data/jugadores.dat', 'wb') as f:
            pickle.dump(self.jugadores, f, protocol=2)
