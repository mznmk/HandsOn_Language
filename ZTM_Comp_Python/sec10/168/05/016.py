# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%205.md

print(*(i*i for i in tuple(map(int, input().split(","))) if i%2), sep=",")
