from functools import reduce


def multiply_by2(item):
    return item * 2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    return acc + item


my_list = [1, 2, 3]

print(list(map(multiply_by2, my_list)))
print(list(map(lambda item: item*2, my_list)))

print(list(filter(only_odd, my_list)))
print(list(filter(lambda item: item%2, my_list)))

print(reduce(accumulator, my_list, 0))
print(reduce(lambda acc, item: acc+item, my_list, 0))

print(my_list)
