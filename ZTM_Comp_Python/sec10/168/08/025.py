# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%208.md

class Uma():
    _name = "Uma"

    def __init__(self, name=None):
        self._name = name

    def print_name(self):
        print(f"Name: {self._name}")


ai = Uma()
ai.print_name()

sw = Uma("Special Week")
sw.print_name()

oc = Uma()
oc._name = "Oguri Cap"
oc.print_name()
