from Autor import *
class Libro:
    def __init__ (self, titulo, isbn):
        self.Titulo = titulo
        self.ISBN = isbn
    def AñadirAutor(self, autor):
        self.Autor = autor
    def MostrarLibro(self):
        print("------ Libro ------")
        print("Titulo: ",self.Titulo)
        print("ISBN: ", self.ISBN)
        self.Autor.MostrarAutor()
        print("-------------------")
    def ObtenerTitulo(self):
        return self.Titulo;
    def ObtenerIsbn(self):
        return self.ISBN;
