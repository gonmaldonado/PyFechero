from Libro import *
import pickle 
class Biblioteca:
    def __init__(self):
        with open("Fichero.pickle", "rb") as f:
            obj = pickle.load(f)
        self.ListaLibros = obj
       #self.ListaLibros = []
    def NumeroLibros(self):
        return len(self.ListaLibros)
    def AñadirLibro(self,libro):
        self.ListaLibros = self.ListaLibros + [libro]
        with open("Fichero.pickle", "wb") as f:
            pickle.dump(self.ListaLibros, f)
    def MostrarBiblioteca(self):
        print("########################################")
        for item in self.ListaLibros:
            item.MostrarLibro()
            print("########################################")
    def BorrarLibro(self, isbn):
        encontrado = False
        posicionaborrar = -1
        for item in self.ListaLibros:
            posicionaborrar += 1
            if item.ObtenerIsbn() == isbn:
                encontrado = True
                break
        if encontrado:
            del self.ListaLibros[posicionaborrar]
            with open("Fichero.pickle", "wb") as f:
                pickle.dump(self.ListaLibros, f)
            print("¡Libro borrado correctamente!")
        else:
            print("¡Libro no encontrado!")
