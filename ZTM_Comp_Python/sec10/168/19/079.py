# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_19.md

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

for sub in subjects:
    for verb in verbs:
        for obj in objects:
            print(f"{sub} {verb} {obj}.")
