import random

class Pregunta:

    def __init__(self, contenido, categoria, respuestas):
        self.contenido = contenido
        self.categoria = categoria
        self.respuestas = respuestas
        random.shuffle(self.respuestas)

    def obtener_contenido(self):
        return self.contenido

    def obtener_respuestas(self):
        return self.respuestas
