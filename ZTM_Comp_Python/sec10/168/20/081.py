# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_20.md

li = [12, 24, 35, 70, 88, 120, 155]
li = list(filter(lambda x: not (x%5==0 and x%7==0), li))
print(li)
