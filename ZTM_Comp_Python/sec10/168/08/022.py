# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%208.md

words = input().split(" ")
d = dict()
for word in words:
    if word not in d.keys():
        d[word] = 1
    else:
        d[word] += 1

d = list(d.items())
d.sort()
for k, v in d:
    print(f"{k}:{v}")
