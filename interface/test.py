import sys
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.ttk as ttk

from PIL import Image,ImageTk

class ventana_ronda:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.botonNuevo1 = tk.Button(self.root)
        self.botonNuevo1.place(x=500, y=100)
        img = Image.open('../data/retroceder.png')
        img = img.resize((50, 50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.botonNuevo1.configure(image=img)
        self.botonNuevo1.pack()
        self.root.mainloop()

    def iniciar(self):
        self.root.mainloop()

ventana_ronda = ventana_ronda()
