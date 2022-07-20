# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day%202.md

class InputOutString(object):
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

str_obj = InputOutString()
str_obj.get_string()
str_obj.print_string()