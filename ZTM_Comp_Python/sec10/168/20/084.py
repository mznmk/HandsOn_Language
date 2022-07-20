# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_20.md

li = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(3)]
for x in range(3):
    for y in range(5):
        print(li[x][y])
    print()