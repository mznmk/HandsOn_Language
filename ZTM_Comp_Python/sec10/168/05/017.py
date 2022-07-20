# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%205.md

logs = []
while 1:
    log = input()
    if len(log)==0:
        break
    dw, am = log.split(" ")
    am = int(am)
    logs.append([dw, am])

amount = 0
for dw, am in logs:
    if dw == "D":
        amount += am
    elif dw == "W":
        if amount - am >= 0:
            amount -= am

print(amount)
