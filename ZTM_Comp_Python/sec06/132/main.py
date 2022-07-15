class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("logged in")

    def attack(self):
        print("do nothing")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f"attacking with power of {self.power}")


wizard1 = Wizard("Merlin", 50)
print(dir(wizard1))
