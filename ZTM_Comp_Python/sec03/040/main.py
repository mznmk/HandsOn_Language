import getpass

username = input("what is your username?: ")
password = getpass.getpass("what is your password?: ")

print(f'{username}, your password, {password}, is {len(password)} letters long')

password_length = len(password)
hidden_password = "*" * password_length

print(f'{username}, your password, {hidden_password}, is {password_length} letters long')
