# tarea.py
class Tarea:
    def __init__(self, descripcion, completada=False):
        self.descripcion = descripcion
        self.completada = completada

    def completar(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

    def to_dict(self):
        return {'descripcion': self.descripcion, 'completada': self.completada}

    @staticmethod
    def from_dict(data):
        return Tarea(data['descripcion'], data['completada'])
