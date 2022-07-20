# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%201.md

def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

n = int(input())
ans = fact(n)
print(ans)