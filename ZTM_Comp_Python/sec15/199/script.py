import random


def run_guess(guess, answer):
    if 1 <= guess <= 10:
        if guess == answer:
            print("you are geneius!")
            return True
    else:
        print("hey bozo, I said 1~10")
        return False


if __name__ == "__main__":
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input("guess a number 1~10: "))
            if run_guess(guess, answer):
                break
        except ValueError:
            print("please enter number")
            continue
