# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_16.md

def func1(n:int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return func1(n-1) + func1(n-2)

func2 = lambda x: 0 if x==0 else 1 if x==1 else func2(x-1)+func2(x-2)

n = int(input())
print(func1(n))
print(func2(n))
