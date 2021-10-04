import sys
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk

class VentanaInicio:
    def __init__(self, concurso, interfaz):

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        _fuenteMont11 = '-family {Montserrat SemiBold} -size 11 -weight bold'

        self.ventana = tk.Tk()
        self.style = ttk.Style()
        self.concurso = concurso
        self.interfaz = interfaz
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.ventana.geometry("500x500+600+100")
        self.ventana.resizable(0,  0)
        self.ventana.title("Concurso de preguntas")
        self.ventana.configure(background="#484848")
        self.ventana.configure(highlightbackground="#d9d9d9")
        self.ventana.configure(highlightcolor="black")
    
        self.botonIniciar = tk.Button(self.ventana)
        self.botonIniciar.place(relx=0.32, rely=0.411, height=37, width=160)
        self.botonIniciar.configure(text='''Iniciar''')
        self.botonIniciar.configure(command=self.boton_iniciar)

        self.botonEditor = tk.Button(self.ventana)
        self.botonEditor.place(relx=0.32, rely=0.513, height=37, width=160)
        self.botonEditor.configure(command=self.boton_editor)
        self.botonEditor.configure(text='''Editor''')

        self.botonOpciones = tk.Button(self.ventana)
        self.botonOpciones.place(relx=0.32, rely=0.616, height=37, width=160)
        self.botonOpciones.configure(command=self.boton_opciones)
        self.botonOpciones.configure(text='''Opciones''')

        self.botonSalir = tk.Button(self.ventana)
        self.botonSalir.place(relx=0.32, rely=0.821, height=37, width=160)
        self.botonSalir.configure(command=self.cerrar)
        self.botonSalir.configure(text='''Salir''')

        self.botonesMenu = [self.botonIniciar,  self.botonEditor,
                            self.botonOpciones,  self.botonSalir]

        for botonMenu in self.botonesMenu:
            botonMenu.configure(font=_fuenteMont11, takefocus="")

        self.menubar = tk.Menu(self.ventana,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.ventana.configure(menu = self.menubar)

        self.Label1 = tk.Label(self.ventana)
        self.Label1.place(relx=0.12, rely=0.103, height=101, width=374)
        self.Label1.configure(activebackground="#f0f0f0f0f0f0")
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Perpetua Titling MT} -size 17 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''CONCURSO DE PREGUNTAS''')

        self.ventana.mainloop()

    def boton_iniciar(self):
        self.cerrar()
        self.concurso.iniciar()
        self.interfaz.crear_ventana_ronda()

    def boton_editor(self):
        self.cerrar()
        self.interfaz.crear_ventana_editor()

    def boton_opciones(self):
        pass

    def cerrar(self):
        self.ventana.destroy()
        self.ventana = None
