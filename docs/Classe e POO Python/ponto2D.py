# TODO: Falta implementar hashcode

class Ponto2D:
    def __init__(self, x: float, y: float):
        self._x = float(x)
        self._y = float(y)

    @classmethod
    def from_str(cls, ponto: str):
        coords = ponto.strip().split(',')
        return cls(float(coords[0][1:]), float(coords[1][:-1]))
    
    @property 
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x
        return self
        
    @property 
    def y(self):
        return self._y
        
    @y.setter 
    def y(self, new_y):
        self._y = new_y
        return self
        
    def __eq__(self, p) -> bool:
        if type(self) is type(p):
            return self.x == p.x and self.y == p.y        
        return NotImplemented

    def __add__(self, p) -> 'Ponto2D':
        return Ponto2D(self.x + p.x, self.y + p.y)

    def __str__(self):
        return f'<{self.x},{self.y}>'
    
    def __repr__(self):
        class_name = type(self).__qualname__
        return f'{class_name}({self.x}, {self.y})'



p1, p2 = Ponto2D(1, 2), Ponto2D(4, 1)
print(p1 + p2 == Ponto2D(5, 3))


class Ponto2D_V2(Ponto2D):
    contador = 0

    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        Ponto2D_V2.contador += 1

p3 = Ponto2D_V2(1, 2)
print(p3.contador)
p4 = Ponto2D_V2(3, 5)
print(p3.contador, p4.contador)
p5 = Ponto2D_V2(3, 5)
print(p3.contador, p4.contador, p5.contador)


