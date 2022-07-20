# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_17.md

def validate(data: list) -> None:
    for v in data:
        assert v % 2 == 0, f"{v} is not even number."


data1 = [2, 4, 6, 8]
data2 = [2, 4, 6, 9]
validate(data1)
validate(data2)
