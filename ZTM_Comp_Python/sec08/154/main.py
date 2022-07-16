# decorator
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("***************")
        func(*args, **kwargs)
        print("***************")
        print()
    return wrap_func


@my_decorator
def hello(arg1, arg2, kwarg1=":("):
    print(arg1, arg2, kwarg1)

hello("helloo!", "mika")
hello("helloo!", "mika", ":)")

