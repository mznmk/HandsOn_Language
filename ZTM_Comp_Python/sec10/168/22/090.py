# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_22.md

s = input()

d = dict()
for c in s:
    # if c in d.keys():
    #     d[c] += 1
    # else:
    #     d[c] = 1
    d[c] = d.get(c, 0) + 1

for k, v in d.items():
    print(f"{k},{v}")
