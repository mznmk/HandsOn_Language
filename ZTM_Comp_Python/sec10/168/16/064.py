# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_16.md

def gen(n: int) -> int:
    for i in range(0, n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i


n = int(input())
li = [i for i in gen(n)]
print(*li, sep=",")