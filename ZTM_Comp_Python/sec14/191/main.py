import re

string = "search this inside of this text please!"

a = re.search("this", string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())

pattern1 = re.compile("this")
b = pattern1.search(string)
c = pattern1.findall(string)
pattern2 = re.compile("search this inside")
d = pattern2.fullmatch(string)
e = pattern2.match(string)
print(b.group())
print(c)
print(d)
print(e)
