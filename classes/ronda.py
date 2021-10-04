import random

class Ronda:

    def __init__(self, id, categoria, premio):
        self.id = id
        self.categoria = categoria
        self.premio = premio



    def obtener_id(self):
        return self.id

    def obtener_categoriao(self):
        return self.categoria

    def obtener_premio(self):
        return self.premio

    def obtener_pregunta_aleatoria(self):
        return random.choice(self.categoria.obtener_preguntas())
