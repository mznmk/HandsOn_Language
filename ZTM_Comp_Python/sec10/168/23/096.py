# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_23.md

import textwrap

s = input()
n = int(input())

# strings = textwrap.wrap(s, n)
# for string in strings:
#     print(string)

strings = textwrap.fill(s, n)
print(strings)
