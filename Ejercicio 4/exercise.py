
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
    