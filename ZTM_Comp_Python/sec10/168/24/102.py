# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_24.md

s = input()

d, l = 0, 0
for c in s:
    if c.isdigit():
        d += 1
    elif c.isalpha():
        l += 1

print(f"Digit - {d}")
print(f"Letter - {l}")
