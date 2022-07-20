# https://github.com/darkprinx/break-the-ice-with-python/blob/master/Status/Day_22.md

def solver(heads: int, legs: int) -> int:
    solutions = []
    for i in range(0, heads+1):
        c = i
        r = heads - i
        if 2*c + 4*r == legs:
            solutions.append([c, r])
    return solutions


heads = 35
legs = 94
solutions = solver(heads, legs)
for chickens, rabbits in solutions:
    print(f"chickens: {chickens} rabbits: {rabbits}")
