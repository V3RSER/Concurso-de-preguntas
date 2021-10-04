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

class VentanaRegistro:
    def __init__(self, jugadores, interfaz):
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
        self.jugadores = jugadores
        self.interfaz = interfaz
        self.jugador_actual = 0
        self.registro_actual = 0

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
        self.textoMenu1.configure(text='''Jugador''')

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
        self.textoMenu2.configure(text='''Registro''')

        self.textoRegistro = tk.Label(self.ventana)
        self.textoRegistro.place(x=50, y=125, height=100, width=400)
        self.textoRegistro.configure(background=_colorFondo)
        self.textoRegistro.configure(font=_fuenteMont12)
        self.textoRegistro.configure(foreground="#000000")
        self.textoRegistro.configure(highlightbackground=_colorFondo)
        self.textoRegistro.configure(highlightcolor="black")
        self.textoRegistro.configure(relief="groove")
        self.textoRegistro.configure(justify='left')

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

        self.botonEliminar = tk.Button(self.ventana)
        self.botonEliminar.place(x=227+(60+15)*2, y=240, height=40, width=60)
        self.botonEliminar.configure(takefocus="")
        self.botonEliminar.configure(bg=_colorMenu)
        self.botonEliminar.configure(activebackground=_colorBotonPresionado)
        self.botonEliminar.configure(cursor="hand2")
        self.botonEliminar.configure(command=self.boton_eliminar)
        imagenEliminar = Image.open('images/basura.png')
        imagenEliminar = imagenEliminar.resize((25, 25), Image.ANTIALIAS)
        imagenEliminar = ImageTk.PhotoImage(imagenEliminar)
        self.botonEliminar.configure(image=imagenEliminar)

        self.textoNombre = tk.Label(self.ventana)
        self.textoNombre.configure(activebackground="#f9f9f9")
        self.textoNombre.configure(activeforeground="black")
        self.textoNombre.configure(anchor='center')
        self.textoNombre.configure(background=_colorMenu)
        self.textoNombre.configure(borderwidth="1")
        self.textoNombre.configure(disabledforeground="#a3a3a3")
        self.textoNombre.configure(font="-family {Montserrat SemiBold} -size 11 -weight bold")
        self.textoNombre.configure(foreground="#ffffff")
        self.textoNombre.configure(highlightcolor="black")
        self.textoNombre.configure(text='''Nombre''')

        self.textoRecord = tk.Label(self.ventana)
        self.textoRecord.configure(activebackground="#f9f9f9")
        self.textoRecord.configure(activeforeground="black")
        self.textoRecord.configure(anchor='center')
        self.textoRecord.configure(background=_colorMenu)
        self.textoRecord.configure(borderwidth="1")
        self.textoRecord.configure(disabledforeground="#a3a3a3")
        self.textoRecord.configure(font="-family {Montserrat SemiBold} -size 11 -weight bold")
        self.textoRecord.configure(foreground="#ffffff")
        self.textoRecord.configure(highlightcolor="black")
        self.textoRecord.configure(text='''Record''')

        self.textoBilletera = tk.Label(self.ventana)
        self.textoBilletera.configure(activebackground="#f9f9f9")
        self.textoBilletera.configure(activeforeground="black")
        self.textoBilletera.configure(anchor='center')
        self.textoBilletera.configure(background=_colorMenu)
        self.textoBilletera.configure(borderwidth="1")
        self.textoBilletera.configure(disabledforeground="#a3a3a3")
        self.textoBilletera.configure(font="-family {Montserrat SemiBold} -size 11 -weight bold")
        self.textoBilletera.configure(foreground="#ffffff")
        self.textoBilletera.configure(highlightcolor="black")
        self.textoBilletera.configure(text='''textoBilletera''')
        self.textosEstadisticas = [self.textoNombre, self.textoRecord, self.textoBilletera]
        y = 320
        for textoEstadistica in self.textosEstadisticas:
            textoEstadistica.configure(font=_fuenteMont12)
            textoEstadistica.place(x=60, y=y, height=40, width=400)
            y += 60

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
        self.botonAtrasMenu1.configure(command=self.anterior_jugador)

        self.botonAdelanteMenu1 = tk.Button(self.ventana)
        self.botonAdelanteMenu1.place(x=xMenu1 + 429, y=yMenu1 + 3, height=46, width=68)
        self.botonAdelanteMenu1.configure(takefocus="")
        self.botonAdelanteMenu1.configure(bg=_colorMenu)
        self.botonAdelanteMenu1.configure(activebackground=_colorBotonPresionado)
        self.botonAdelanteMenu1.configure(image=imagenAdelante)
        self.botonAdelanteMenu1.configure(command=self.siguiente_jugador)

        self.botonAtrasMenu2 = tk.Button(self.ventana)
        self.botonAtrasMenu2.place(x=xMenu2 + 3, y=yMenu2 + 3, height=46, width=68)
        self.botonAtrasMenu2.configure(takefocus="")
        self.botonAtrasMenu2.configure(bg=_colorMenu)
        self.botonAtrasMenu2.configure(activebackground=_colorBotonPresionado)
        self.botonAtrasMenu2.configure(cursor="hand2")
        self.botonAtrasMenu2.configure(image=imagenAtras)
        self.botonAtrasMenu2.configure(command=self.anterior_registro)

        self.botonAdelanteMenu2 = tk.Button(self.ventana)
        self.botonAdelanteMenu2.place(x=xMenu2 + 429, y=yMenu2 + 3, height=46, width=68)
        self.botonAdelanteMenu2.configure(takefocus="")
        self.botonAdelanteMenu2.configure(bg=_colorMenu)
        self.botonAdelanteMenu2.configure(activebackground=_colorBotonPresionado)
        self.botonAdelanteMenu2.configure(image=imagenAdelante)
        self.botonAdelanteMenu2.configure(command=self.siguiente_registro)

        self.menubar = tk.Menu(self.ventana,font="TkMenuFont",bg=_colorFondo,fg=_fgcolor)
        self.ventana.configure(menu = self.menubar)

        self.actualizar_ventana()
        self.ventana.mainloop()

    def boton_eliminar(self):
        if len(self.obtener_registros_actuales()) > 1:
            self.obtener_jugador_actual().elminiar_registro(self.obtener_registro_actual())
            self.actualizar_ventana()

    def actualizar_ventana(self):
        jugador = self.obtener_jugador_actual()
        registro = self.obtener_registro_actual()
        registros = self.obtener_registros_actuales()

        self.textoMenu1.configure(text=f"Jugador: {jugador.obtener_nombre()}")
        self.textoMenu2.configure(
            text=f"Registro: {registros.index(registro)+1}")
        self.textoRegistro.configure(text=registro.obtener_contenido())
        self.textoNombre.configure(text=f"Nombre: {jugador.obtener_nombre()}")
        record  = registros[0].obtener_dinero_ganado()
        for registro in self.obtener_registros_actuales():
            if record < registro.obtener_dinero_ganado():
                record = registro.obtener_dinero_ganado()
        self.textoRecord.configure(text=f"Record: {record}")
        self.textoBilletera.configure(text=f"Billetera: {jugador.obtener_billetera()}")

    def siguiente_jugador(self):
        if self.categoria_jugador < (len(self.jugadores) - 1):
            self.categoria_jugador += 1
            self.registro_actual = 0
            self.actualizar_ventana()

    def anterior_jugador(self):
        if self.jugador_actual > 0:
            self.jugador_actual -= 1
            self.registro_actual = 0
            self.actualizar_ventana()

    def siguiente_registro(self):
        if self.registro_actual < len(self.obtener_registros_actuales()) - 1:
            self.registro_actual += 1
            self.actualizar_ventana()

    def anterior_registro(self):
        if self.registro_actual > 0:
            self.registro_actual -= 1
            self.actualizar_ventana()

    def obtener_registro_actual(self):
       return self.obtener_registros_actuales()[self.registro_actual]

    def obtener_registros_actuales(self):
        return self.obtener_jugador_actual().obtener_registros()

    def obtener_jugador_actual(self):
        return self.jugadores[self.jugador_actual]

    def boton_hogar(self):
        self.ventana.destroy()
        self.ventana = None
        self.interfaz.guardar_jugadores()
        self.interfaz.crear_ventana_inicio()