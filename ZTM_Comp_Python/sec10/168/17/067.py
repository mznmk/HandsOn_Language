# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_17.md

def binary_search(data: list, n: int):
    ok = len(data)-1
    ng = 0
    while ok-ng > 1:
        mid = (ok+ng)//2
        if n <= data[mid]:
            ok = mid
        else:
            ng = mid
    return ok


n = int(input())
data = [1, 5, 8, 10, 12, 13, 55, 66, 73, 78, 82, 85, 88, 99]
print(binary_search(data, n))
