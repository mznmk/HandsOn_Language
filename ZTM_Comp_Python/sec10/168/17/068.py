# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_17.md

import random
import math


def shake1():
    r = math.floor(random.random() * 100)
    if 10 <= r <= 100:
        return r
    else:
        return shake1()


def shake2():
    return math.floor(random.random() * 90) + 10


print(shake1())
print(shake2())
