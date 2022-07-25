import re

# validate password
pattern = re.compile(r"(^[A-Za-z0-9$%#@]{8,}$)")
string1 = "Aho$%1234#@Boke"
string2 = "Aa0$"
string3 = "aho==boke"

password1 = pattern.fullmatch(string1)
print(password1)
password2 = pattern.fullmatch(string2)
print(password2)
password3 = pattern.fullmatch(string3)
print(password3)
