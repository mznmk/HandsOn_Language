from functools import reduce


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

my_list = [1, 2, 3]
your_list = (10, 20, 30)
their_list = (5, 4, 3)
print(reduce(accumulator, my_list, 0))
print(my_list)
print(your_list)
print(their_list)
