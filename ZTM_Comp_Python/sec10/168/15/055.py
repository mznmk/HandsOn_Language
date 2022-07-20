# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_15.md

import re

line = input()
pattern = "\d+"
ans = re.findall(pattern, line)
print(ans)
