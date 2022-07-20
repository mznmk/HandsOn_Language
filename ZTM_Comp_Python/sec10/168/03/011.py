# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%203.md

# case 1
def check(binary):
    if int(binary, 2) % 5 == 0:
        return True
    return False

binarys = input().split(",")
binarys = list(filter(check, binarys))
print(*binarys, sep=",")

# case 2
print(*(b for b in input().split(",") if int(b,2)%5==0), sep=",")