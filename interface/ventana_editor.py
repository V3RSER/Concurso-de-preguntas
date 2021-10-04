import pickle
import sys
from tkinter import INSERT, END

from PIL import Image, ImageTk

from classes.pregunta import Pregunta
from classes.respuesta import Respuesta

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk

class VentanaEditor:
    def __init__(self, categorias, interfaz):
        _colorFondo = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        _colorMenu = '#232323'
        _colorBotonPresionado = '#505050'
        _fuenteMont10 = '-family {Montserrat SemiBold} -size 10 -weight bold'
        _fuenteMont11 = '-family {Montserrat SemiBold} -size 11 -weight bold'
        _fuenteMont12 = '-family {Montserrat SemiBold} -size 12 -weight bold'

        self.ventana = tk.Tk()
        self.style = ttk.Style()
        self.categorias = categorias
        self.interfaz = interfaz
        self.categoria_actual = 0
        self.pregunta_actual = 0

        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_colorFondo)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _colorFondo), ('active',_ana2color)])

        self.ventana.geometry("500x500+600+100")
        self.ventana.resizable(0,  0)
        self.ventana.title("Concurso de preguntas")
        self.ventana.configure(background="#484848")
        self.ventana.configure(highlightbackground=_colorFondo)
        self.ventana.configure(highlightcolor="black")

        xMenu1 = 0
        yMenu1 = 0
        xMenu2 = 0
        yMenu2 = 53

        self.textoMenu1 = tk.Label(self.ventana)
        self.textoMenu1.place(x=xMenu1, y=yMenu1, height=50, width=500)
        self.textoMenu1.configure(activebackground="#f9f9f9")
        self.textoMenu1.configure(activeforeground="black")
        self.textoMenu1.configure(anchor='center')
        self.textoMenu1.configure(background=_colorMenu)
        self.textoMenu1.configure(borderwidth="1")
        self.textoMenu1.configure(disabledforeground="#a3a3a3")
        self.textoMenu1.configure(font="-family {Montserrat SemiBold} -size 13 -weight bold")
        self.textoMenu1.configure(foreground="#ffffff")
        self.textoMenu1.configure(highlightbackground=_colorFondo)
        self.textoMenu1.configure(highlightcolor="black")
        self.textoMenu1.configure(text='''Categoría''')

        self.textoMenu2 = tk.Label(self.ventana)
        self.textoMenu2.place(x=xMenu2, y=yMenu2, height=50, width=500)
        self.textoMenu2.configure(activebackground="#f9f9f9")
        self.textoMenu2.configure(activeforeground="black")
        self.textoMenu2.configure(anchor='center')
        self.textoMenu2.configure(background=_colorMenu)
        self.textoMenu2.configure(borderwidth="1")
        self.textoMenu2.configure(disabledforeground="#a3a3a3")
        self.textoMenu2.configure(font="-family {Montserrat SemiBold} -size 13 -weight bold")
        self.textoMenu2.configure(foreground="#ffffff")
        self.textoMenu2.configure(highlightbackground=_colorFondo)
        self.textoMenu2.configure(highlightcolor="black")
        self.textoMenu2.configure(text='''Pregunta''')

        self.textoPregunta = tk.Text(self.ventana)
        self.textoPregunta.place(x=50, y=125, height=100, width=400)
        self.textoPregunta.configure(background=_colorFondo)
        self.textoPregunta.configure(font=_fuenteMont12)
        self.textoPregunta.configure(foreground="#000000")
        self.textoPregunta.configure(highlightbackground=_colorFondo)
        self.textoPregunta.configure(highlightcolor="black")
        self.textoPregunta.configure(relief="groove")

        self.botonHogar = tk.Button(self.ventana)
        self.botonHogar.place(x=227-(60+15)*2, y=240, height=40, width=60)
        self.botonHogar.configure(takefocus="")
        self.botonHogar.configure(bg=_colorMenu)
        self.botonHogar.configure(activebackground=_colorBotonPresionado)
        self.botonHogar.configure(cursor="hand2")
        self.botonHogar.configure(command=self.boton_hogar)
        imagenHogar = Image.open('images/hogar.png')
        imagenHogar = imagenHogar.resize((25, 25), Image.ANTIALIAS)
        imagenHogar = ImageTk.PhotoImage(imagenHogar)
        self.botonHogar.configure(image=imagenHogar)

        self.botonAgregar = tk.Button(self.ventana)
        self.botonAgregar.place(x=227-60-15, y=240, height=40, width=60)
        self.botonAgregar.configure(takefocus="")
        self.botonAgregar.configure(bg=_colorMenu)
        self.botonAgregar.configure(activebackground=_colorBotonPresionado)
        self.botonAgregar.configure(cursor="hand2")
        self.botonAgregar.configure(command=self.boton_agregar)
        imagenAgregar = Image.open('images/agregar.png')
        imagenAgregar = imagenAgregar.resize((25, 25), Image.ANTIALIAS)
        imagenAgregar = ImageTk.PhotoImage(imagenAgregar)
        self.botonAgregar.configure(image=imagenAgregar)

        self.botonGuardar = tk.Button(self.ventana)
        self.botonGuardar.place(x=227, y=240, height=40, width=60)
        self.botonGuardar.configure(takefocus="")
        self.botonGuardar.configure(bg=_colorMenu)
        self.botonGuardar.configure(activebackground=_colorBotonPresionado)
        self.botonGuardar.configure(cursor="hand2")
        self.botonGuardar.configure(command=self.boton_guardar)
        imagenGuardar = Image.open('images/guardar.png')
        imagenGuardar = imagenGuardar.resize((25, 25), Image.ANTIALIAS)
        imagenGuardar = ImageTk.PhotoImage(imagenGuardar)
        self.botonGuardar.configure(image=imagenGuardar)

        self.botonEliminar = tk.Button(self.ventana)
        self.botonEliminar.place(x=227+60+15, y=240, height=40, width=60)
        self.botonEliminar.configure(takefocus="")
        self.botonEliminar.configure(bg=_colorMenu)
        self.botonEliminar.configure(activebackground=_colorBotonPresionado)
        self.botonEliminar.configure(cursor="hand2")
        self.botonEliminar.configure(command=self.boton_eliminar)
        imagenEliminar = Image.open('images/basura.png')
        imagenEliminar = imagenEliminar.resize((25, 25), Image.ANTIALIAS)
        imagenEliminar = ImageTk.PhotoImage(imagenEliminar)
        self.botonEliminar.configure(image=imagenEliminar)

        self.botonReestablecer = tk.Button(self.ventana)
        self.botonReestablecer.place(x=227+(60+15)*2, y=240, height=40, width=60)
        self.botonReestablecer.configure(takefocus="")
        self.botonReestablecer.configure(bg=_colorMenu)
        self.botonReestablecer.configure(activebackground=_colorBotonPresionado)
        self.botonReestablecer.configure(cursor="hand2")
        self.botonReestablecer.configure(command=self.boton_reestablecer)
        imagenReestablecer = Image.open('images/reiniciar.png')
        imagenReestablecer = imagenReestablecer.resize((25, 25), Image.ANTIALIAS)
        imagenReestablecer = ImageTk.PhotoImage(imagenReestablecer)
        self.botonReestablecer.configure(image=imagenReestablecer)

        # ---------------------------- respuestas ----------------------------#

        self.textoRespuesta0 = tk.Text(self.ventana)
        self.textoRespuesta1 = tk.Text(self.ventana)
        self.textoRespuesta2 = tk.Text(self.ventana)
        self.textoRespuesta3 = tk.Text(self.ventana)
        self.textosRespuesta = [self.textoRespuesta0, self.textoRespuesta1,
                                 self.textoRespuesta2, self.textoRespuesta3]

        imagenValida = tk.PhotoImage(width=66, height=33)
        imagenErrada = tk.PhotoImage(width=66, height=33)
        imagenValida.put(("green",), to=(32, 32, 66, 0))
        imagenErrada.put(("red",), to=(0, 0, 32, 32))

        self.vars_check_respuesta = [
            tk.IntVar(value=0), tk.IntVar(value=0), tk.IntVar(value=0), tk.IntVar(value=0)]

        self.checkRespuesta0 = tk.Checkbutton(self.ventana)
        self.checkRespuesta0.configure(
            command=lambda:self.actualizar_tipo_respuesta(self.vars_check_respuesta[0]),
            variable=self.vars_check_respuesta[0])
        self.checkRespuesta1 = tk.Checkbutton(self.ventana)
        self.checkRespuesta1.configure(
            command=lambda: self.actualizar_tipo_respuesta(self.vars_check_respuesta[1]),
            variable=self.vars_check_respuesta[1])
        self.checkRespuesta2 = tk.Checkbutton(self.ventana)
        self.checkRespuesta2.configure(
            command=lambda: self.actualizar_tipo_respuesta(self.vars_check_respuesta[2]),
            variable=self.vars_check_respuesta[2])
        self.checkRespuesta3 = tk.Checkbutton(self.ventana)
        self.checkRespuesta3.configure(
            command=lambda: self.actualizar_tipo_respuesta(self.vars_check_respuesta[3]),
            variable=self.vars_check_respuesta[3])
        self.checksRespuesta = [self.checkRespuesta0, self.checkRespuesta1,
                                self.checkRespuesta2, self.checkRespuesta3]

        self.checkRespuesta0.configure(
            image=imagenErrada, selectimage=imagenValida,
            indicatoron=False, onvalue=1, offvalue=0)

        y = 295
        for textoRespuesta, checkRespuesta in zip(self.textosRespuesta, self.checksRespuesta):
            textoRespuesta.configure(font=_fuenteMont11, wrap="word")
            textoRespuesta.place(x=50, y=y, height=37, width=313)
            checkRespuesta.configure(
                image=imagenErrada, selectimage=imagenValida,
                indicatoron=False, onvalue=True, offvalue=False)
            checkRespuesta.place(x=376, y=y, height=37, width=74)
            y += 50
        # --------------------------------------------------------------------#

        imagenAdelante = Image.open('images/adelante.png')
        imagenAdelante = imagenAdelante.resize((25, 25), Image.ANTIALIAS)
        imagenAdelante = ImageTk.PhotoImage(imagenAdelante)

        imagenAtras = Image.open('images/atras.png')
        imagenAtras = imagenAtras.resize((25, 25), Image.ANTIALIAS)
        imagenAtras = ImageTk.PhotoImage(imagenAtras)

        self.botonAtrasMenu1 = tk.Button(self.ventana)
        self.botonAtrasMenu1.place(x=xMenu1 + 3, y=yMenu1 + 3, height=46, width=68)
        self.botonAtrasMenu1.configure(takefocus="")
        self.botonAtrasMenu1.configure(bg=_colorMenu)
        self.botonAtrasMenu1.configure(activebackground=_colorBotonPresionado)
        self.botonAtrasMenu1.configure(cursor="hand2")
        self.botonAtrasMenu1.configure(image=imagenAtras)
        self.botonAtrasMenu1.configure(command=self.anterior_categoria)

        self.botonAdelanteMenu1 = tk.Button(self.ventana)
        self.botonAdelanteMenu1.place(x=xMenu1 + 429, y=yMenu1 + 3, height=46, width=68)
        self.botonAdelanteMenu1.configure(takefocus="")
        self.botonAdelanteMenu1.configure(bg=_colorMenu)
        self.botonAdelanteMenu1.configure(activebackground=_colorBotonPresionado)
        self.botonAdelanteMenu1.configure(image=imagenAdelante)
        self.botonAdelanteMenu1.configure(command=self.siguiente_categoria)

        self.botonAtrasMenu2 = tk.Button(self.ventana)
        self.botonAtrasMenu2.place(x=xMenu2 + 3, y=yMenu2 + 3, height=46, width=68)
        self.botonAtrasMenu2.configure(takefocus="")
        self.botonAtrasMenu2.configure(bg=_colorMenu)
        self.botonAtrasMenu2.configure(activebackground=_colorBotonPresionado)
        self.botonAtrasMenu2.configure(cursor="hand2")
        self.botonAtrasMenu2.configure(image=imagenAtras)
        self.botonAtrasMenu2.configure(command=self.anterior_pregunta)

        self.botonAdelanteMenu2 = tk.Button(self.ventana)
        self.botonAdelanteMenu2.place(x=xMenu2 + 429, y=yMenu2 + 3, height=46, width=68)
        self.botonAdelanteMenu2.configure(takefocus="")
        self.botonAdelanteMenu2.configure(bg=_colorMenu)
        self.botonAdelanteMenu2.configure(activebackground=_colorBotonPresionado)
        self.botonAdelanteMenu2.configure(image=imagenAdelante)
        self.botonAdelanteMenu2.configure(command=self.siguiente_pregunta)

        self.menubar = tk.Menu(self.ventana,font="TkMenuFont",bg=_colorFondo,fg=_fgcolor)
        self.ventana.configure(menu = self.menubar)

        self.actualizar_ventana()
        self.ventana.mainloop()

    def boton_agregar(self):
        pregunta = Pregunta("", self.obtener_categoria_actual(), [
                            Respuesta("", "valida"),
                            Respuesta("", "errada"),
                            Respuesta("", "errada"),
                            Respuesta("", "errada")])
        self.pregunta_actual = len(self.obtener_preguntas_actuales()) - 1
        self.actualizar_ventana()

    def boton_eliminar(self):
        self.obtener_categoria_actual().eliminar_pregunta(self.obtener_pregunta_actual())
        if len(self.obtener_preguntas_actuales()) == 0:
            self.boton_agregar()
        self.actualizar_ventana()

    def boton_guardar(self):
        contenido_pregunta = self.textoPregunta.get("1.0", END).rstrip()
        respuestas = []
        for numero, textoRespuesta in zip(range(0, 4), self.textosRespuesta):
            if self.vars_check_respuesta[numero].get():
                respuestas.append(Respuesta(textoRespuesta.get("1.0", END).rstrip(), "valida"))
            else:
                respuestas.append(Respuesta(textoRespuesta.get("1.0", END).rstrip(), "errada"))
        self.obtener_pregunta_actual().establecer_contenido(contenido_pregunta)
        self.obtener_pregunta_actual().establecer_respuestas(respuestas)
        preguntas = [self.categorias[0].obtener_preguntas(),
                     self.categorias[1].obtener_preguntas(),
                     self.categorias[2].obtener_preguntas(),
                     self.categorias[3].obtener_preguntas(),
                     self.categorias[4].obtener_preguntas()]
        with open('data/preguntas.dat', 'wb') as f:
            pickle.dump([preguntas], f, protocol=2)

    def siguiente_categoria(self):
        if self.categoria_actual < (len(self.categorias) - 1):
            self.categoria_actual += 1
            self.pregunta_actual = 0
            self.actualizar_ventana()

    def anterior_categoria(self):
        if self.categoria_actual > 0:
            self.categoria_actual -= 1
            self.pregunta_actual = 0
            self.actualizar_ventana()

    def siguiente_pregunta(self):
        if self.pregunta_actual < len(self.obtener_preguntas_actuales())- 1:
            self.pregunta_actual += 1
            self.actualizar_ventana()

    def anterior_pregunta(self):
        if self.pregunta_actual > 0:
            self.pregunta_actual -= 1
            self.actualizar_ventana()

    def obtener_pregunta_actual(self):
        #print(f"self.obtener_preguntas_actuales(){self.obtener_preguntas_actuales()}")
        #print(f"self.[self.pregunta_actual](){self.pregunta_actual}")

        return self.obtener_preguntas_actuales()[self.pregunta_actual]

    def obtener_preguntas_actuales(self):
        return self.obtener_categoria_actual().obtener_preguntas()

    def obtener_categoria_actual(self):
        return self.categorias[self.categoria_actual]

    def actualizar_ventana(self):
        categoria = self.obtener_categoria_actual().obtener_dificultad()

        pregunta = self.obtener_pregunta_actual()
        respuestas = pregunta.obtener_respuestas()
        self.textoMenu1.configure(text=f"Categoría: {categoria}")
        self.textoMenu2.configure(
            text=f"Pregunta: {self.obtener_preguntas_actuales().index(pregunta)+1}")
        self.textoPregunta.delete("1.0", END)
        self.textoPregunta.insert(INSERT, pregunta.obtener_contenido())
        for numero, textoRespuesta in zip(range(0, 4), self.textosRespuesta):
            textoRespuesta.delete("1.0", END)
            textoRespuesta.insert(INSERT, respuestas[numero].obtener_contenido())
            if respuestas[numero].obtener_tipo() == 'valida':
                self.checksRespuesta[numero].invoke()

    def actualizar_tipo_respuesta(self, check_pulsado):
        for var in self.vars_check_respuesta:
            if var == check_pulsado:
                var.set(1)
            else:
                var.set(0)

    def boton_hogar(self):
        self.ventana.destroy()
        self.ventana = None
        self.interfaz.crear_ventana_inicio()

    def boton_reestablecer(self):
        self.categorias[0].agregar_preguntas([])
        self.categorias[1].agregar_preguntas([])
        self.categorias[2].agregar_preguntas([])
        self.categorias[3].agregar_preguntas([])
        self.categorias[4].agregar_preguntas([])

        Pregunta("¿Quién descubrió América?", self.categorias[0], [
                Respuesta("Cristóbal Colón", "valida"),
                Respuesta("Simón Bolívar", "errada"),
                Respuesta("Rafael Nuñez", "errada"),
                Respuesta("Antonio Nariño", "errada")
        ])
        Pregunta("¿A cuánto equivale el numero Pi?", self.categorias[0], [
                Respuesta("3.1416", "valida"),
                Respuesta("3.1614", "errada"),
                Respuesta("3.1514", "errada"),
                Respuesta("3.1615  ", "errada")
        ])
        Pregunta("¿Cuál es el animal más rápido del mundo?", self.categorias[0], [
                Respuesta("Guepardo", "valida"),
                Respuesta("Cóndor", "errada"),
                Respuesta("Leopardo", "errada"),
                Respuesta("Avestruz", "errada")
        ])
        Pregunta("¿Cómo se llama el proceso por medio del cual las plantas obtienen su alimento?", self.categorias[0], [
                Respuesta("Fotosíntesis", "valida"),
                Respuesta("Biosíntesis", "errada"),
                Respuesta("Luminosíntesis", "errada"),
                Respuesta("Biosíntesos", "errada")
        ])
        Pregunta("¿Cómo se le denomina al centro de un átomo?", self.categorias[0], [
                Respuesta("Núcleo", "valida"),
                Respuesta("Electrón", "errada"),
                Respuesta("Protón", "errada"),
                Respuesta("Quark", "errada")
        ])
        Pregunta("¿Cuántos días hay en un año bisiesto?", self.categorias[1], [
                Respuesta("366", "valida"),
                Respuesta("365", "errada"),
                Respuesta("364", "errada"),
                Respuesta("355", "errada")
        ])
        Pregunta("¿Cuál es el animal más grande del mundo?", self.categorias[1], [
                Respuesta("La ballena azul", "valida"),
                Respuesta("El elefante", "errada"),
                Respuesta("La jirafa", "errada"),
                Respuesta("El cachalote", "errada")
        ])
        Pregunta("¿Cuántas patas tiene la araña?", self.categorias[1], [
                Respuesta("8", "valida"),
                Respuesta("6", "errada"),
                Respuesta("10", "errada"),
                Respuesta("12", "errada")
        ])
        Pregunta("¿Quién era el general de los Nazis en la Segunda Guerra Mundial?", self.categorias[1], [
                Respuesta("Adolf Hitler", "valida"),
                Respuesta("Heinrich Himmler", "errada"),
                Respuesta("Benito Mussolini", "errada"),
                Respuesta("Boris Becker", "errada")
        ])
        Pregunta("¿Cuál fue el primer hombre en ir a la luna?", self.categorias[1], [
                Respuesta("Neil Armstrong", "valida"),
                Respuesta("Louis Armstrong", "errada"),
                Respuesta("Michael Armstrong", "errada"),
                Respuesta("Lance Armstrongr", "errada")
        ])
        Pregunta("¿Cuál es el primero de la lista de los números primos?", self.categorias[2], [
                Respuesta("2", "valida"),
                Respuesta("0", "errada"),
                Respuesta("1", "errada"),
                Respuesta("3", "errada")
        ])
        Pregunta("¿Cuál es el océano más grande del mundo?", self.categorias[2], [
                Respuesta("Océano Pacífico", "valida"),
                Respuesta("Océano Índico", "errada"),
                Respuesta("Océano Atlántico", "errada"),
                Respuesta("Océano Ártico", "errada")
        ])
        Pregunta("¿Quién era el dios griego de la guerra?", self.categorias[2], [
                Respuesta("Ares", "valida"),
                Respuesta("Zeus", "errada"),
                Respuesta("Marte", "errada"),
                Respuesta("Hades", "errada")
        ])
        Pregunta("¿Cuál es el país más grande del mundo?", self.categorias[2], [
                Respuesta("Rusia", "valida"),
                Respuesta("China", "errada"),
                Respuesta("India", "errada"),
                Respuesta("Canadá", "errada")
        ])
        Pregunta("¿Cuál es la nación más pequeña del mundo?", self.categorias[2], [
                Respuesta("El Vaticano", "valida"),
                Respuesta("Mónaco", "errada"),
                Respuesta("Andorra", "errada"),
                Respuesta("Portugal", "errada")
        ])
        Pregunta("¿Quién es el padre del psicoanálisis?", self.categorias[3], [
                Respuesta("Sigmund Freud", "valida"),
                Respuesta("Carl Gustav Jung", "errada"),
                Respuesta("Skinner", "errada"),
                Respuesta("Viktor Frankl", "errada")
        ])
        Pregunta("¿Quién escribió La Odisea?", self.categorias[3], [
                Respuesta("Homero", "valida"),
                Respuesta("Virgilio", "errada"),
                Respuesta("Cervantes", "errada"),
                Respuesta("Kafka", "errada")
        ])
        Pregunta("¿Cuál es la obra más importante de la literatura en español?", self.categorias[3], [
                Respuesta("Don Quijote de la Mancha", "valida"),
                Respuesta("El Principito", "errada"),
                Respuesta("Cien años de soledad", "errada"),
                Respuesta("Romeo y Julieta", "errada")
        ])
        Pregunta("¿Quién pintó La noche estrellada?", self.categorias[3], [
                Respuesta("Vincent van Gogh", "valida"),
                Respuesta("Rembrandt", "errada"),
                Respuesta("Velazquez", "errada"),
                Respuesta("Leonardo da Vinci", "errada")
        ])
        Pregunta("¿¿Cuál es la única ciudad que está en dos continentes distintos??", self.categorias[3], [
                Respuesta("Estambul", "valida"),
                Respuesta("Moscú", "errada"),
                Respuesta("Berlín   ", "errada"),
                Respuesta("Denver", "errada")
        ])
        Pregunta("¿Cómo se llama la estrofa poética que está conformada por 10 versos de 8 sílabas cada uno?",
                 self.categorias[4], [
                     Respuesta("Décima espinela", "valida"),
                     Respuesta("Decasílabo", "errada"),
                     Respuesta("Decasílabo octogonal", "errada"),
                     Respuesta("Décima octava", "errada")
         ])
        Pregunta("¿En qué parte del cuerpo se produce la insulina?", self.categorias[4], [
            Respuesta("Páncreas", "valida"),
            Respuesta("Hígado", "errada"),
            Respuesta("Cerebro", "errada"),
            Respuesta("Pulmones", "errada")
        ])
        Pregunta("¿Cuántos corazones tienen los pulpos?", self.categorias[4], [
            Respuesta("3", "valida"),
            Respuesta("1", "errada"),
            Respuesta("2", "errada"),
            Respuesta("4", "errada")
        ])
        Pregunta("¿Dónde va más rápido el tiempo?", self.categorias[4], [
            Respuesta("Centro de la Tierra", "valida"),
            Respuesta("Cima del Everest", "errada"),
            Respuesta("La Luna", "errada"),
            Respuesta("Fosas Marianas", "errada")
        ])
        Pregunta("¿Qué es un pulsar?", self.categorias[4], [
            Respuesta("Estrella de neutrones", "valida"),
            Respuesta("Fusión de dos agujeros negros", "errada"),
            Respuesta("Planeta que envía señales", "errada"),
            Respuesta("Agujero negro naciente", "errada")
        ])
        self.categoria_actual = 0
        self.pregunta_actual = 0
        self.actualizar_ventana()
