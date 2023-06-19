from Biblioteca import *
def MostrarMenu():
        print ("""Menu
                1) Añadir libro a la biblioteca
                2) Mostrar biblioteca
                3) Borrar libro
                4) ¿Numero de libros?
                5) Salir""")
def AñadirLibroABiblioteca(biblioteca):
        titulo = input("Introduzca el titulo del libro: ")
        isbn = input("Introduzca el ISBN del libro: ")
        autornombre = input("Introduzca el nombre del autor: ")
        autorapellidos = input("Introduzca el apellido del autor: ")
        autor = Autor(autornombre,autorapellidos)
        libro = Libro(titulo, isbn)
        libro.AñadirAutor(autor)
        biblioteca.AñadirLibro(libro)
        return biblioteca
def MostrarBiblioteca(biblioteca):
        biblioteca.MostrarBiblioteca()
def BorrarLibro(biblioteca):
        isbn = input("Introduzca el titulo del ISBN a borrar: ")
        biblioteca.BorrarLibro(isbn)
def NumeroLibros(biblioteca):
        print("El numero de libros en la biblioteca es: ",biblioteca.NumeroLibros())
fin = False
biblioteca = Biblioteca()
while not fin:
        MostrarMenu()
        opcion = int(input("Seleccione opcion:"))
        if(opcion == 1):
            biblioteca = AñadirLibroABiblioteca(biblioteca)
        elif(opcion == 2):
            MostrarBiblioteca(biblioteca)
        elif(opcion == 3):
            BorrarLibro(biblioteca)
        elif(opcion == 4):
            NumeroLibros(biblioteca)
        elif(opcion == 5):
            fin = True
            print("¡Adios!")