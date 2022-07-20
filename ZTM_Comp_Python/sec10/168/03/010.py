# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%203.md

words = input().split(" ")
words = list(set(words))
words.sort()
print(*words, sep=" ")
