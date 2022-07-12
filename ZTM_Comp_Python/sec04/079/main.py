picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
fill = "$"
space = " "
empty = ""

def show_tree(picture, fill, space, empty):
    for row in picture:
        for pixel in row:
            if pixel == 0:
                print(space, end="")
            elif 1 == 1:
                print(fill, end="")
        print(empty, end="\n")

show_tree(picture, fill, space, empty)
show_tree(picture, fill, space, empty)
show_tree(picture, fill, space, empty)