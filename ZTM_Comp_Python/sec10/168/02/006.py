# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%202.md

from math import sqrt, floor

C, H = 50, 30

def calc(d):
    d = int(d)
    q = floor(sqrt((2*C*d)/H))
    return q

D = list(map(calc, input().split(",")))
print(*D, sep=",")
