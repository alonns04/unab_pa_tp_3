from exercise import Cancion

a = Cancion("Las habladurías del mundo","L. A. Spinetta")

b = Cancion("","123")

print(b.titulo,b.autor)
print(a.get_titulo())
print(a.get_autor())