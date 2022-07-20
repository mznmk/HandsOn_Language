def gen_fun(num):
    for i in range(num):
        yield i

for item in gen_fun(100):
    print(item)