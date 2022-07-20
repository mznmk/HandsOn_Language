# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_16.md

def func1(n: int) -> int:
    if n == 0:
        return 0
    return func1(n-1)+100

func2 = lambda x: func2(x-1)+100 if x > 0 else 0

n = int(input())
print(func1(n))
print(func2(n))
