class Punto():
    def _init_(self, x, y):
        self.x = x
        self.y = y
        
    def imprimir(self):
        print((self.x,self.y))
        
    def eje_x(self):
        return self.x
        
    def eje_y(self):
        return self.y
        
    def opuesto(self):
        return Punto(-self.eje_x(),-self.eje_y())