class Autor:
    def __init__ (self, nombre, apellidos):
        self.Nombre = nombre
        self.Apellidos = apellidos
    def MostrarAutor(self):
        print("Autor: ",self.Nombre," ",self.Apellidos)