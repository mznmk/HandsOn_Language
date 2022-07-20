# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%206.md

stats = []
while 1:
    stat = input()
    if not stat:
        break
    name, age, score = stat.split(",")
    stats.append((name, int(age), int(score)))

stats.sort(key=lambda x: (x[0], x[1], x[2]))
print(stats)