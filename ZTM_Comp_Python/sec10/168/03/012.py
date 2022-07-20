# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%203.md

def check(n):
    judge = True
    n = str(n)
    for c in n:
        if int(c)%2:
            judge = False
            break
    return judge

l = 1000
r = 3000
nums = list(filter(check,range(l, r+1)))
print(*nums, sep=",")