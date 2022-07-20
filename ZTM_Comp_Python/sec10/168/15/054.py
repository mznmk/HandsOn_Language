# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_15.md

import re

email = "john@google.com elise@yahoo.com"
pattern = "\w+@(\w+)\.com"
ans = re.findall(pattern, email)
print(ans)

