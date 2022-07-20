# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_23.md

m = int(input())
a = list(map(int, input().split()))
n = int(input())
b = list(map(int, input().split()))

xor = list(set(a) ^ set(b))
xor.sort()
for v in xor:
    print(v)
