# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%202.md

X, Y = map(int, input().split(","))

grid = [[y for y in range(Y)] for _ in range(X)]
for i in range(X):
    for j in range(Y):
        grid[i][j] *= i

print(grid)
