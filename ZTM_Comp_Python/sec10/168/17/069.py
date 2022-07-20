# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_17.md

from random import random


def shake():
    return random() * 90.0 + 5.0


print(shake())
