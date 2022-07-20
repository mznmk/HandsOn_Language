# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_24.md

n = int(input())
words = [input() for _ in range(n)]

d = dict()
for word in words:
    d[word] = d.get(word, 0) + 1

vs = d.values()
print(*vs)
