import sys
from PIL import Image, ImageTk

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk

class VentanaRonda:
    def __init__(self, concurso, interfaz):
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
        self.concurso = concurso
        self.interfaz = interfaz
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

        self.textoRonda = tk.Label(self.ventana)
        self.textoRonda.place(x=0, y=0, height=50, width=250)
        self.textoRonda.configure(activebackground="#f9f9f9")
        self.textoRonda.configure(activeforeground="black")
        self.textoRonda.configure(anchor='w')
        self.textoRonda.configure(background=_colorMenu)
        self.textoRonda.configure(borderwidth="125")
        self.textoRonda.configure(disabledforeground="#a3a3a3")
        self.textoRonda.configure(font="-family {Montserrat SemiBold} -size 13 -weight bold")
        self.textoRonda.configure(foreground="#ffffff")
        self.textoRonda.configure(highlightbackground=_colorFondo)
        self.textoRonda.configure(highlightcolor="black")
        self.textoRonda.configure(text='''Ronda''')

        self.textoDinero = tk.Label(self.ventana)
        self.textoDinero.place(relx=0.5, rely=0.0, height=50, width=250)
        self.textoDinero.configure(activebackground="#f9f9f9")
        self.textoDinero.configure(activeforeground="#000000")
        self.textoDinero.configure(anchor='w')
        self.textoDinero.configure(background="#232323")
        self.textoDinero.configure(borderwidth="45")
        self.textoDinero.configure(compound='right')
        self.textoDinero.configure(disabledforeground="#a3a3a3")
        self.textoDinero.configure(font="-family {Montserrat SemiBold} -size 13 -weight bold")
        self.textoDinero.configure(foreground="#ffffff")
        self.textoDinero.configure(highlightbackground=_colorFondo)
        self.textoDinero.configure(highlightcolor="black")
        imagenDinero = Image.open('images/dinero.png')
        imagenDinero = imagenDinero.resize((25, 25), Image.ANTIALIAS)
        imagenDinero = ImageTk.PhotoImage(imagenDinero)
        self.textoDinero.configure(image=imagenDinero)
        self.textoDinero.configure(justify='right')
        self.textoDinero.configure(padx="5")
        self.textoDinero.configure(text='''0''')

        self.botonHogar = tk.Button(self.ventana)
        self.botonHogar.place(x=3, y=3, height=46, width=68)
        self.botonHogar.configure(takefocus="")
        self.botonHogar.configure(bg=_colorMenu)
        self.botonHogar.configure(activebackground=_colorBotonPresionado)
        self.botonHogar.configure(cursor="hand2")
        self.botonHogar.configure(command=self.boton_hogar)
        imagenHogar = Image.open('images/hogar.png')
        imagenHogar = imagenHogar.resize((25, 25), Image.ANTIALIAS)
        imagenHogar = ImageTk.PhotoImage(imagenHogar)
        self.botonHogar.configure(image=imagenHogar)

        self.botonAdelante = tk.Button(self.ventana)
        self.botonAdelante.place(x=429, y=3, height=46, width=68)
        self.botonAdelante.configure(takefocus="")
        self.botonAdelante.configure(bg=_colorMenu)
        self.botonAdelante.configure(command=self.actualizar_ventana)
        self.botonAdelante.configure(activebackground=_colorBotonPresionado)

        imagenAdelante = Image.open('images/adelante.png')
        imagenAdelante = imagenAdelante.resize((25, 25), Image.ANTIALIAS)
        imagenAdelante = ImageTk.PhotoImage(imagenAdelante)
        self.botonAdelante.configure(image=imagenAdelante)

        self.textoPregunta = tk.Label(self.ventana)
        self.textoPregunta.place(x=50, y=100, height=100, width=400)
        self.textoPregunta.configure(activebackground="#f9f9f9")
        self.textoPregunta.configure(activeforeground="black")
        self.textoPregunta.configure(background=_colorFondo)
        self.textoPregunta.configure(disabledforeground="#a3a3a3")
        self.textoPregunta.configure(font=_fuenteMont12)
        self.textoPregunta.configure(foreground="#000000")
        self.textoPregunta.configure(highlightbackground=_colorFondo)
        self.textoPregunta.configure(highlightcolor="black")
        self.textoPregunta.configure(relief="ridge")

        # ---------------------------- respuestas ----------------------------#

        self.botonRespuesta0 = tk.Button(self.ventana)
        self.botonRespuesta0.configure(command=lambda:self.verificar_respuesta(self.botonRespuesta0))

        self.botonRespuesta1 = tk.Button(self.ventana)
        self.botonRespuesta1.configure(command=lambda:self.verificar_respuesta(self.botonRespuesta1))

        self.botonRespuesta2 = tk.Button(self.ventana)
        self.botonRespuesta2.configure(command=lambda:self.verificar_respuesta(self.botonRespuesta2))

        self.botonRespuesta3 = tk.Button(self.ventana)
        self.botonRespuesta3.configure(command=lambda:self.verificar_respuesta(self.botonRespuesta3))

        self.botonesRespuesta = [self.botonRespuesta0, self.botonRespuesta1,
                                 self.botonRespuesta2, self.botonRespuesta3]

        y = 250+50-37
        for botonRespuesta in self.botonesRespuesta:
            botonRespuesta.configure(font=_fuenteMont11, takefocus="")
            botonRespuesta.place(x=50, y=y, height=37, width=400)
            y += 55
        # --------------------------------------------------------------------#

        self.menubar = tk.Menu(self.ventana,font="TkMenuFont",bg=_colorFondo,fg=_fgcolor)
        self.ventana.configure(menu = self.menubar)

        self.actualizar_ventana()
        self.ventana.mainloop()

    def actualizar_ventana(self):
        ronda = self.concurso.obtener_ronda_actual()
        pregunta = self.concurso.obtener_pregunta_actual()
        respuestas = pregunta.obtener_respuestas()

        if ronda.obtener_id() == 1:
            self.ventana.configure(background="#265161")
        elif ronda.obtener_id() == 2:
            self.ventana.configure(background="#2C5E28")
        elif ronda.obtener_id() == 3:
            self.ventana.configure(background="#685C31")
        elif ronda.obtener_id() == 4:
            self.ventana.configure(background="#5C3823")
        elif ronda.obtener_id() == 5:
            self.ventana.configure(background="#511515")

        self.textoRonda.configure(text=f"Ronda {ronda.obtener_id()}")
        self.textoPregunta.configure(text=pregunta.obtener_contenido())
        self.botonAdelante.configure(state='disabled', cursor='arrow')

        for numero, boton in zip(range(0, 4), self.botonesRespuesta):
            boton.configure(text=respuestas[numero].obtener_contenido(),
                            cursor="hand2", state='normal', bg='#d9d9d9')

    def verificar_respuesta(self, boton_pulsado):
        for numero, boton in zip(range(0, 4), self.botonesRespuesta):
            boton.configure(state='disabled', cursor='arrow')
            if boton_pulsado == boton:
                if self.concurso.confirmar_respuesta(numero):
                    boton.configure(bg="#0dff31")
                    self.respuesta_correcta()
                else:
                    boton.configure(bg="#e82025")
                    self.respuesta_incorrecta()

    def respuesta_incorrecta(self):
        self.textoPregunta.configure(text="I N C O R R E C T O")

    def respuesta_correcta(self):
        self.textoPregunta.configure(text="C O R R E C T O")
        self.botonAdelante.configure(cursor="hand2", state='normal')
        self.textoDinero.configure(text=self.concurso.obtener_dinero_actual())

    def boton_hogar(self):
        self.ventana.destroy()
        self.ventana = None
        self.interfaz.crear_ventana_inicio()