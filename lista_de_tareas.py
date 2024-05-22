# lista_de_tareas.py
import json
from tarea import Tarea

class ListaDeTareas:
    def __init__(self, archivo="tareas.json"):
        self.tareas = []
        self.archivo = archivo
        self.cargar_tareas()

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        self.guardar_tareas()

    def completar_tarea(self, indice):
        try:
            self.tareas[indice].completar()
            self.guardar_tareas()
        except IndexError:
            raise ValueError("Índice de tarea no válido")

    def eliminar_tarea(self, indice):
        try:
            del self.tareas[indice]
            self.guardar_tareas()
        except IndexError:
            raise ValueError("Índice de tarea no válido")

    def mostrar_tareas(self):
        return [str(tarea) for tarea in self.tareas]

    def guardar_tareas(self):
        with open(self.archivo, 'w') as file:
            json.dump([tarea.to_dict() for tarea in self.tareas], file)

    def cargar_tareas(self):
        try:
            with open(self.archivo, 'r') as file:
                tareas_data = json.load(file)
                self.tareas = [Tarea.from_dict(tarea) for tarea in tareas_data]
        except FileNotFoundError:
            self.tareas = []
