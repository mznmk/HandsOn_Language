# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%202.md

words = input().split(",")
words.sort()
print(*words, sep=",")
