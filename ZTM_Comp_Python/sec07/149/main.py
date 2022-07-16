some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates1 = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates1:
            duplicates1.append(value)
print(duplicates1)

duplicates2 = list({x for x in some_list if some_list.count(x) > 1})
print(duplicates2)
