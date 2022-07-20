# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_19.md

from time import time

before = time()
for _ in range(10**5):
    1 + 1
after = time()
print(f"exec: {after-before} ms")
