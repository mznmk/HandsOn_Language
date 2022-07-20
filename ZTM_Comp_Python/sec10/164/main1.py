from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        res = fn()
        t2 = time()
        print(f"took {t2-t1} ms")
        return res
    return wrapper

@performance
def long_time1():
    print("1")
    for i in range(10**8):
        i*5

@performance
def long_time2():
    print("2")
    for i in list(range(10**8)):
        i*5

long_time1()
long_time2()