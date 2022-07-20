# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_13.md

from math import pi


class Circle():
    def __init__(self, r):
        self._radius = r

    def area(self):
        return self._radius**2 * pi


circle = Circle(2)
print(circle.area())
