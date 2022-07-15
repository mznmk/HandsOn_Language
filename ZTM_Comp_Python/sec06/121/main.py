class PlayerCharacter:
    membership = True

    def __init__(self, name="anonymous", age=0):
        self.name = name
        self.age = age

    def shout(self):
        print(f"my name is {self.name}")

    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


# print(PlayerCharacter.adding_things(2, 3))
player1 = PlayerCharacter.adding_things(2, 3)
print(player1.name, player1.age)
print(PlayerCharacter.adding_things2(2, 3))
