def highest_even(li):
    evens = []
    for v in li:
        if v%2==0:
            evens.append(v)
    return max(evens)

print(highest_even([1, 2, 3, 4, 8, 10, 11]))