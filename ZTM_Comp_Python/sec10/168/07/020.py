# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%207.md

class MyGen():
    def seven(self, n):
        for i in range(0, n//7+1):
            yield i*7

n = int(input())
for v in MyGen().seven(n):
    print(v)