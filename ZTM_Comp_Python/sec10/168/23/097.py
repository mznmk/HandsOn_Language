# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_23.md

import string


def main():
    # [ input / create data ]
    n = int(input())
    size = 1 + (n-1)*4
    yo = xo = size//2
    alpha = string.ascii_lowercase

    # [ guard crouse ]
    if not 1 <= n <= 26:
        return

    # [ create grid ]
    grid = [["-" for _ in range(size)] for _ in range(size)]

    # [ draw rangoli ]
    vb = -(n-1)
    vt = n-1
    for i in range(vb, vt+1):
        y = yo + i*2
        hl = -(n-1 - abs(i))
        hr = n-1 - abs(i)
        for j in range(hl, hr+1):
            idx = abs(i) + abs(j)
            x = xo + j*2
            grid[y][x] = alpha[idx]

    # [ for debug ]
    # print(alpha)
    # print(xo, yo)

    # [ output ]
    for row in grid:
        print(*row, sep="")

    # [ return ]
    return


if __name__ == "__main__":
    main()
