class Categoria:

    def __init__(self, dificultad, id):
        self.dificultad = dificultad
        self.id = id
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def obtener_preguntas(self):
        return self.preguntas