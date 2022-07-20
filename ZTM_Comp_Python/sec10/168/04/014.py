# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%204.md

s = input()

u, l = 0, 0
for c in s:
    if c.isupper():
        u += 1
    elif c.islower():
        l +=1

print(f"UPPER CASE {u}")
print(f"LOWER CASE {l}")