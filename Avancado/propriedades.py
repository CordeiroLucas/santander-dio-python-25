class Foo:
    def __init__(self, x=None):
        self._x = x
    
    @property   
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be non-negative")
        self._x += value
    
    @x.deleter
    def x(self):
        self._x = 0
    
foo = Foo(6)
print(foo.x)

foo.x = 3
print(foo.x)

del foo.x

print(foo.x)