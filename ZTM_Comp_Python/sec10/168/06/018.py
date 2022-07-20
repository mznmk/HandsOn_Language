# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%206.md

def check(password:str):
    up, low, num, sym = 0, 0, 0, 0
    for c in password:
        if c.isupper():
            up += 1
        elif c.islower():
            low += 1
        elif c.isdigit():
            num += 1
        elif c in ["$", "#", "@"]:
            sym += 1
    if not 6 <= len(password) <= 12:
        return False
    elif not (up and low and num and sym):
        return False
    return True

passwords = input().split(",")
passwords = list(filter(check, passwords))
print(*passwords, sep=",")
