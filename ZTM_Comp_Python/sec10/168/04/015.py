# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%204.md

n = input()

# case 1
ans = 0
num = ""
for _ in range(4):
    num += n
    ans += int(num)

print(ans)

# case 2
print(sum([int(n*i) for i in range(1, 4+1)]))
