class Concurso:

    def __init__(self, rondas, jugador):
        self.rondas = rondas
        self.jugador = jugador

    def iniciar(self):
        self.n_ronda_actual = 0
        self.pregunta_actual = None
        self.jugador.establecer_dinero(0)
        self.selecionar_pregunta()

    def finalizar(self, condicion):
        self.jugador.generar_registro(condicion)

    def confirmar_respuesta(self, numero):
        respuesta = self.pregunta_actual.obtener_respuestas()[numero].obtener_tipo()
        if respuesta == "valida": return True
        else: return False

    def aumentarRonda(self):
        self.otorgar_premio()
        self.n_ronda_actual += 1
        if self.n_ronda_actual > 4:
            self.n_ronda_actual = 4
        else:
            self.selecionar_pregunta()

    def selecionar_pregunta(self):
        self.pregunta_actual = self.obtener_ronda_actual().obtener_pregunta_aleatoria()

    def otorgar_premio(self):
        self.jugador.agregar_premio(self.obtener_ronda_actual().obtener_premio())

    def obtener_ronda_actual(self):
        return self.rondas[self.n_ronda_actual]

    def obtener_pregunta_actual(self):
        return self.pregunta_actual

    def obtener_jugador(self):
        return self.jugador

    def obtener_dinero_actual(self):
        return self.jugador.obtener_dinero()

    def obtener_rondas(self):
        return self.rondas