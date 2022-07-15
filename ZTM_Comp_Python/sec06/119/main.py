class PlayerCharacter:
    membership = True
    def __init__(self, name="anonymous", age=0):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f"my name is {self.name}")


player1 = PlayerCharacter("cindy", 16)
player2 = PlayerCharacter("tom", 21)

print(player1.shout())
print(player2.shout())
