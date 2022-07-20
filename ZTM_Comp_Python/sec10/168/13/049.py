# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_13.md

class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self._length = length

    def area(self):
        return self._length**2


shape = Shape()
print(shape.area())
square = Square(5)
print(square.area())
