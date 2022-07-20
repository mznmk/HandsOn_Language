# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_24.md

def func(n):
    if n == 0:
        return 0
    return func(n-1) + n


n = int(input())
print(func(n))
