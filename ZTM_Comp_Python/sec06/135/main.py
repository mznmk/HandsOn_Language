class User:
    def sign_in(self):
        print("logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f"{self.num_arrows} remainging")

    def run(self):
        print("ran really fast")

class HybridBord(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)


hb1 = HybridBord("borgie", 50, 100)
hb1.sign_in()
hb1.attack()
hb1.check_arrows()
hb1.run()