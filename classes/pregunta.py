import random

class Pregunta:

    def __init__(self, contenido, categoria, respuestas):
        self.contenido = contenido
        categoria.agregar_pregunta(self)
        self.categoria = categoria.obtener_id()
        self.respuestas = respuestas
        random.shuffle(self.respuestas)

    def establecer_contenido(self, contenido):
        self.contenido = contenido

    def establecer_respuestas(self, respuestas):
        self.respuestas = respuestas

    def obtener_contenido(self):
        return self.contenido

    def obtener_respuestas(self):
        return self.respuestas
