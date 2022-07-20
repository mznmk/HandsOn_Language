# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%202.md

lines = []

while True:
    line = input()
    if len(line)==0:
        break
    lines.append(line.upper())

for line in lines:
    print(line)
