def sum(num1, num2):
    def func(n1, n2):
        return n1 + n2
    return func(num1, num2)

print(sum(4, 5))