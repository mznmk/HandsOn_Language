# decorator
from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        res = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1} ms")
        return res
    return wrapper

@performance
def long_time():
    for i in range(10**8):
        i*5

long_time()