# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_21.md

class Person():
    def __init__(self):
        self._gender = "Unknown"

    def getGender(self):
        return self._gender


class Male(Person):
    def __init__(self):
        Person.__init__(self)
        self._gender = "Male"


class Female(Person):
    def __init__(self):
        Person.__init__(self)
        self._gender = "Female"


person = Person()
print(person.getGender())
male = Male()
print(male.getGender())
female = Female()
print(female.getGender())
