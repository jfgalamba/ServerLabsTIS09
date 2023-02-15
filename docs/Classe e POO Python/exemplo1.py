class X:
    def __init__(self, a):
        self.a = a
    
    def metodo1(self, i):
        return self.a + i

class Y(X):
    pass

class Z(X):
    def __init__(self, b, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.b = b

    def metodo1(self, i):
        return super().metodo1(i) + self.b + 1

obj1 = X(10)
obj2 = Y(10)
obj3 = Z(15, 10)

for obj in (obj1, obj2, obj3):
    print(type(obj).__name__, obj.metodo1(3))
