def fib(memo:list, n:int) -> None:
    if memo[n] != -1:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    res = fib(memo, n-1) + fib(memo, n-2)
    memo[n] = res
    return res

n = 20
memo = [-1] * (n+1)
print(fib(memo, n))