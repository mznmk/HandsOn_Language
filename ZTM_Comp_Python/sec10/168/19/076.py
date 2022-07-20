# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_19.md

import zlib

s = "hello world!hello world!hello world!hello world!"
b = bytes(s, "utf-8")
c = zlib.compress(b)
print(c)
print(zlib.decompress(c))
