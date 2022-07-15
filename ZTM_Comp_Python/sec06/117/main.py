class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")


player1 = PlayerCharacter("cindy", 44)
player1.attack = 50
player2 = PlayerCharacter("tom", 21)

print(player1.name, player1.age)
print(player1.run())
print(player1.attack)
print(player2.name, player2.age)
print(player2.run())
