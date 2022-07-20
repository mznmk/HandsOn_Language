# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_13.md

class Rectangle():
    def __init__(self, length, width) -> None:
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width


rect = Rectangle(4, 3)
print(rect.area())
