# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_20.md

li = [12, 24, 35, 70, 88, 120, 155]
# li = [v for (i, v) in enumerate(li) if not i in [0,2,4,6]]
li = [v for (i, v) in enumerate(li) if not (i%2==0 and i<=6)]
print(li)