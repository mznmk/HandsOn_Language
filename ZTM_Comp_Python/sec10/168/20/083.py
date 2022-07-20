# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_20.md

li = [12, 24, 35, 70, 88, 120, 155]
li = [v for i,v in enumerate(li) if not 1<=i<=3]
print(li)