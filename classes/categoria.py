class Categoria:

    def __init__(self, id, dificultad):
        self.id = id
        self.dificultad = dificultad
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def eliminar_pregunta(self, pregunta):
        self.preguntas.remove(pregunta)

    def agregar_preguntas(self, preguntas):
        self.preguntas = preguntas

    def obtener_preguntas(self):
        return self.preguntas

    def obtener_dificultad(self):
        return self.dificultad

    def obtener_id(self):
        return self.id