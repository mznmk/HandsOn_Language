# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%201.md

print(*(i for i in range(2000, 3201) if i%7==0 and i%5), sep=",")