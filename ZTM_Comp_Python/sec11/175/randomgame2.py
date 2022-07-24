from random import randint
from sys import argv

# const variable
LOW = 3
HIGH = 7


def main():
    # input number
    while True:
        try:
            n: str = input(f"please input number [{LOW}-{HIGH}]: ")
            n = int(n)
            if LOW <= n <= HIGH:
                break
        except ValueError:
            continue
    # generate random number
    r = randint(LOW, HIGH)
    # print input / random
    print(f"input : {n}")
    print(f"random: {r}")
    print()
    # check if input == random
    if n == r:
        print("right number!")
        print()
    else:
        print("wrong number!")
        print("try again!")
        print()
        # retry
        main()


if __name__ == "__main__":
    # update 
    if 2 <= len(argv):
        try:
            LOW = int(argv[1])
        except ValueError:
            pass
    if 3 <= len(argv):
        try:
            HIGH = int(argv[2])
        except ValueError:
            pass
    # exec main()
    main()
