# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_15.md

def func(n: int) -> float:
    ans = 0.0
    for i in range(1, n+1):
        ans += i/(i+1)
    return ans


n = int(input())
print(func(n))
