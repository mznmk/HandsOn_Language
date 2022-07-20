# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_12.md

class American():
    @staticmethod
    def printNationality():
        print("I'm American!")


class NewYorker(American):
    pass


American().printNationality()
NewYorker().printNationality()
