from classes.categoria import Categoria
from classes.concurso import Concurso
from classes.jugador import Jugador
from classes.pregunta import Pregunta
from classes.premio import Premio
from classes.respuesta import Respuesta
from classes.ronda import Ronda
from interface.interfaz import Interfaz
import pickle

if __name__ == '__main__':

    with open('data/jugadores.dat', 'rb') as f:
        jugadores = pickle.load(f)

    categorias = [Categoria(0, "muy fácil"),
                 Categoria(1, "fácil"),
                 Categoria(2, "normal"),
                 Categoria(3, "difícil"),
                 Categoria(4, "muy difícil")]

    with open('data/preguntas.dat', 'rb') as f:
        lista_preguntas = pickle.load(f)
    for categoria, preguntas in zip(categorias, lista_preguntas):
        categoria.agregar_preguntas(preguntas)

    rondas = [Ronda(1, categorias[0], Premio(100)),
              Ronda(2, categorias[1], Premio(300)),
              Ronda(3, categorias[2], Premio(700)),
              Ronda(4, categorias[3], Premio(1500)),
              Ronda(5, categorias[4], Premio(3100))]
    concurso = Concurso(rondas, jugadores[0])
    interfaz = Interfaz(concurso, jugadores)