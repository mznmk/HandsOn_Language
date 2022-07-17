while 1:
    try:
        age = int(input("what is your age?"))
        10/age
    except ValueError:
        print("please enter a number")
        continue
    except ZeroDivisionError:
        print("please enter age higher than 0")
        break
    else:
        print("thank you!")
        break
    finally:
        print("ok I am finally done")
    print("can you hear me?")
