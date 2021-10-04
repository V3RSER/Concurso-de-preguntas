class Respuesta:

    def __init__(self, contenido, tipo):
        self.contenido = contenido
        self.tipo = tipo

    def obtener_contenido(self):
        return self.contenido

    def obtener_tipo(self):
        return self.tipo