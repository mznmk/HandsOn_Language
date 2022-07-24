with open("test1.txt") as file1:
    print(file1.read())
    file1.seek(0)
    print(file1.read())
    file1.seek(0)
    print(file1.read())

with open("test2.txt") as file2:
    # print(file2.readline())
    # print(file2.readline())
    # print(file2.readline())
    print(file2.readlines())
