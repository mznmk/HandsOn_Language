from random import randint

# const variable
LOW = 3
HIGH = 7


def main():
    # input from user
    while True:
        n: str = input(f"please input number [{LOW}-{HIGH}]: ")
        if n.isnumeric():
            n = int(n)
        else:
            continue
        if LOW <= n <= HIGH:
            break
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
        main()


if __name__ == "__main__":
    main()
