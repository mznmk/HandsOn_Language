# decorator
def my_decorator(func):
    def wrap_func():
        print("*************")
        func()
        print("*************")
        print()
    return wrap_func


@my_decorator
def hello1():
    print("hellooooooooo")

hello1()


@my_decorator
def bye1():
    print("see you later")

bye1()


def hello2():
    print("hellooooooooo")

func2 = my_decorator(hello2)
func2()

my_decorator(hello2)()