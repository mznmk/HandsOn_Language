# # write
# with open("sad.txt", mode="w") as file:
#     text = file.write(":(")
#     print(text)

# # read
# with open("./dir/sad.txt", mode="r") as file:
#     print(file.read())

# read
try:
    # with open("sad.txt", mode="r") as file:
    with open("sad.txt", mode="x") as file:
        print(file.read())
except FileNotFoundError as err:
    print("ERROR: file not found error")
    raise err
except IOError as err:
    print("ERROR: IO error")
    raise err