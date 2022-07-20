def generator_function(num):
    for i in range(num):
        yield i*2


# for i in generator_function(100):
#     print(i)

g = generator_function(100)
next(g)
next(g)
next(g)
print(next(g))
print(next(g))
print(next(g))
