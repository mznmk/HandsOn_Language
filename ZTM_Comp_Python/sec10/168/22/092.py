# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_22.md

s = input()

# s = s[::2]
# print(s)

s = [c for i,c in enumerate(s) if i%2==0]
print(*s, sep="")
