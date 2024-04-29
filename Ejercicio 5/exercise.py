"""
Ejercicio 5:
● Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre
cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar
(ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes
servicios: getters y setters, método para leer la información y método para mostrar la
información.
● Este último método mostrará la información del libro con este formato:
Título: Introduction to Java Programming 3a. edición
Autor: Liang, Y. Daniel
ISBN: 0-13-031997-X
Prentice-Hall, New Jersey (USA)
viernes 16 de noviembre de 2001
784 páginas
"""

class Cancion():
    def __init__(self, titulo: str = "", autor: str = ""):
        if not isinstance(titulo, str):
            raise TypeError("El título debe ser una cadena de texto (string)")
        if not isinstance(autor, str):
            raise TypeError("El autor debe ser una cadena de texto (string)")
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.nombre_completo = apellido + ", " + nombre

    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_nombre_completo(self):
        return self.nombre_completo

class Libro:
    def __init__(self, titulo, autor, ISBN, paginas, edicion, editorial, ciudad, pais, fecha_edicion):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.ciudad = ciudad
        self.pais = pais
        self.fecha_edicion = fecha_edicion

    # Getters
    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_ISBN(self):
        return self.ISBN

    def get_paginas(self):
        return self.paginas

    def get_edicion(self):
        return self.edicion

    def get_editorial(self):
        return self.editorial

    def get_ciudad(self):
        return self.ciudad

    def get_pais(self):
        return self.pais

    def get_fecha_edicion(self):
        return self.fecha_edicion

    # Setters
    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    def set_ISBN(self, ISBN):
        self.ISBN = ISBN

    def set_paginas(self, paginas):
        self.paginas = paginas

    def set_edicion(self, edicion):
        self.edicion = edicion

    def set_editorial(self, editorial):
        self.editorial = editorial

    def set_ciudad(self, ciudad):
        self.ciudad = ciudad

    def set_pais(self, pais):
        self.pais = pais

    def set_fecha_edicion(self, fecha_edicion):
        self.fecha_edicion = fecha_edicion

    def mostrar_informacion(self):
        print("Título:", self.titulo, self.edicion, "edición")
        print("Autor:", self.autor)
        print("ISBN:", self.ISBN)
        print(self.editorial + ",", self.ciudad, "(" + self.pais + ")")
        print(self.fecha_edicion)
        print(self.paginas, "páginas")


liang_y_daniel = Persona("Y. Daniel", "Liang")
libro = Libro("Introduction to Java Programming", liang_y_daniel.nombre_completo, "0-13-031997-X", 784, "3a.", "Prentice-Hall", "New Jersey", "USA", "23-12-2004")
libro.mostrar_informacion()