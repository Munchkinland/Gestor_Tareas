import tkinter as tk
from interfaz import Interfaz

class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.interfaz = Interfaz(self.root)

    def ejecutar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
