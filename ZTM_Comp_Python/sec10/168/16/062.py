# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_16.md

def func(memo: list, n: int) -> int:
    if memo[n] != -1:
        return memo[n]
    memo[n] = func(memo, n-1) + func(memo, n-2)
    return memo[n]


n = int(input())
memo = [-1] * (n+1)
memo[0] = 0
memo[1] = 1
func(memo, n)
print(*memo, sep=",")
