# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%207.md

from math import sqrt

moves = {}
while 1:
    move = input()
    if not move:
        break
    dirc, dist = move.split(" ")
    moves[dirc] = int(dist)

y = moves["DOWN"] - moves["UP"]
x = moves["RIGHT"] - moves["LEFT"]
d = round(sqrt(y*y + x*x))
print(d)