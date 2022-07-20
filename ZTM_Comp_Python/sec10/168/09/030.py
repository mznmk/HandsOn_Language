# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%209.md

def print_str(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 > l2:
        print(s1)
    elif l1 < l2:
        print(s2)
    else:
        print(s1)
        print(s2)


s1, s2 = input().split()
print_str(s1, s2)
