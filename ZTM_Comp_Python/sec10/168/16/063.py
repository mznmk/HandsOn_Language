# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_16.md

def gen_even(n: int)-> int:
    for i in range(0, n+1, 2):
        yield i

n = int(input())
even = [i for i in gen_even(n)]
print(*even, sep=",")
