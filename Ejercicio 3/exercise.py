class Linea():

    def  __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def mueve_derecha(distancia: float):    # si no es float genera un error
        distancia = abs(distancia)          # hago que sea positivo, porque mover a la derecha es positivo
        self.p1.mover_x(distancia)
        self.p2.mover_x(distancia)