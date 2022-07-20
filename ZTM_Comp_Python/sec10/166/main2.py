# def fib1(n:int) -> int:
#     a = 0
#     b = 1
#     for i in range(n):
#         yield a
#         tmp = a
#         a = b
#         b = tmp + b

# for x in fib1(21):
#     print(x)


def fib2(n:int) -> int:
    a = 0
    b = 1
    res = []
    for i in range(n):
        res.append(a)
        tmp = a
        a = b
        b = tmp + b
    return res

print(fib2(21))