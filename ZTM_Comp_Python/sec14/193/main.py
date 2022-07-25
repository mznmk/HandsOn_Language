import re

# validate e-mail
pattern1 = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string1 = "aho@boke.com"
string2 = "aho.boke"

email1 = pattern1.search(string1)
print(email1)
email2 = pattern1.search(string2)
print(email2)
