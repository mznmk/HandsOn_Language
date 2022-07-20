# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_24.md

s = input()

d = {}
for c in s:
    d[c] = d.get(c, 0) + 1

l = list(d.items())
l.sort(key=lambda x: (-x[1], x[0]))
for k, v in l:
    print(k, v)
