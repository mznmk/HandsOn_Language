# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_21.md

# li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# li = list(set(li))
# print(li)

def remove_dupl(li:list) -> list:
    newli = []
    for v in li:
        if v not in newli:
            newli.append(v)
    return newli

li = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
li = remove_dupl(li)
print(li)
