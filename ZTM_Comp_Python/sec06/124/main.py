class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")

    def speak(self):
        print(f"my name is {self.name}, I am {self.age} years old")


player1 = PlayerCharacter("mika", "22")
player1.run()
player1.speak()

player2 = PlayerCharacter("mika", "44")
print(player2.name)
print(player2.age)

player3 = {"name": "mika", "age": "44"}
print(player3["name"])
print(player3["age"])
