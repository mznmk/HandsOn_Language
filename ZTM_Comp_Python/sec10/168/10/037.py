# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_10.md

def printlist():
    li = []
    for i in range(1, 20+1):
        li.append(i**2)
    print(tuple(li))


printlist()
