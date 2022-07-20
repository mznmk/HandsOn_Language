# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_18.md

from random import sample

li = [i for i in range(100, 200+1) if i % 2 == 0]
print(sample(li, 5))
