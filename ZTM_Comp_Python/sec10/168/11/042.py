# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_11.md

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sq = list(map(lambda x: x*x, filter(lambda x: x%2==0, li)))
print(sq)
