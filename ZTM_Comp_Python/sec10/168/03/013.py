# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%203.md

s = input()

l, d = 0, 0
for c in s:
    if c.isalpha():
        l += 1
    elif c.isdigit():
        d +=1

print(f"LETTERS {l}")
print(f"DIGITS {d}")