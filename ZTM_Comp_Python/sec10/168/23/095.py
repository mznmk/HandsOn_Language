# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_23.md

n = int(input())
scores = list(set(map(int, input().split())))

scores.sort(reverse=True)
print(scores[1])
