from classes.categoria import Categoria
from classes.concurso import Concurso
from classes.jugador import Jugador
from classes.pregunta import Pregunta
from classes.premio import Premio
from classes.respuesta import Respuesta
from classes.ronda import Ronda
from interface.interfaz import Interfaz


def iniciar(boton_iniciar):
    print(f'iniciar:{boton_iniciar}')

if __name__ == '__main__':
    jugador = Jugador("Luis")
    categoria1 = Categoria("Muy fácil", 1)
    categoria2 = Categoria("Fácil", 2)
    categoria3 = Categoria("Normal", 3)
    categoria4 = Categoria("Difícil", 4)
    categoria5 = Categoria("Muy difícil", 5)
    categoria1.agregar_pregunta(
        Pregunta("¿Quién descubrió América?", categoria1, [
            Respuesta("Cristóbal Colón", "valida"),
            Respuesta("Simón Bolívar", "errada"),
            Respuesta("Rafael Nuñez", "errada"),
            Respuesta("Antonio Nariño", "errada")
    ]))
    categoria2.agregar_pregunta(
        Pregunta("¿Cuántos días hay en un año bisiesto?", categoria2, [
            Respuesta("366", "valida"),
            Respuesta("365", "errada"),
            Respuesta("364", "errada"),
            Respuesta("355", "errada")
    ]))
    categoria3.agregar_pregunta(
        Pregunta("¿Cuántos días hay en un año bisiesto?", categoria3, [
            Respuesta("366", "valida"),
            Respuesta("365", "errada"),
            Respuesta("364", "errada"),
            Respuesta("355", "errada")
        ]))
    categoria4.agregar_pregunta(
        Pregunta("¿Quién es el padre del psicoanálisis?", categoria4, [
            Respuesta("Sigmund Freud", "valida"),
            Respuesta("Carl Gustav Jung", "errada"),
            Respuesta("Skinner", "errada"),
            Respuesta("Viktor Frankl", "errada")
        ]))
    categoria5.agregar_pregunta(
        Pregunta("¿Cómo se llama la estrofa poética que está conformada por 10 versos de 8 sílabas cada uno?", categoria5, [
            Respuesta("Décima espinela", "valida"),
            Respuesta("Decasílabo", "errada"),
            Respuesta("Decasílabo octogonal", "errada"),
            Respuesta("Décima octava", "errada")
        ]))

    ronda1 = Ronda(1, categoria1, Premio(100))
    ronda2 = Ronda(2, categoria2, Premio(300))
    ronda3 = Ronda(3, categoria3, Premio(700))
    ronda4 = Ronda(4, categoria4, Premio(1500))
    ronda5 = Ronda(5, categoria5, Premio(3100))
    concurso = Concurso([ronda1, ronda2, ronda3, ronda4, ronda5], jugador)
    interfaz = Interfaz(concurso)

'''respuesta_jugador = input('Dame una respuesta: ')[:1]
if respuesta_jugador == 'a' or respuesta_jugador == 'A':
    print("es a")
elif respuesta_jugador == 'b' or respuesta_jugador == 'B':
    print("es b")
elif respuesta_jugador == 'c' or respuesta_jugador == 'C':
    print("es c")
elif respuesta_jugador == 'd' or respuesta_jugador == 'D':
    print("es d")'''
