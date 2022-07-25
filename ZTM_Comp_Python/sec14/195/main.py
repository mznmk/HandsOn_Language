import re

# validate password
pattern = re.compile(r"(^[A-Za-z0-9$%#@]{7,}[0-9]$)")
string1 = "Aho$%1234#@Boke"
string2 = "Aho$%1234#@Bok9"
string3 = "abcdefgh"
string4 = "abcdefg0"

password1 = pattern.fullmatch(string1)
print(password1)
password2 = pattern.fullmatch(string2)
print(password2)
password3 = pattern.fullmatch(string3)
print(password3)
password4 = pattern.fullmatch(string4)
print(password4)
