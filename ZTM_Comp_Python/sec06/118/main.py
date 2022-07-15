class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age

    def shout(self):
        print(f"my name is {self.name}")


player1 = PlayerCharacter("cindy", 44)
player1.attack = 50
player2 = PlayerCharacter("tom", 21)

print(player1.shout())
print(player2.shout())
