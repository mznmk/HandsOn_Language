# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_18.md

from random import sample

li = [i for i in range(1, 1000+1) if i % 5 == 0 and i % 7 == 0]
print(sample(li, 5))
