my_set1 = {char for char in "hellooooo"}

print(my_set1)


simple_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}
my_dict1 = {key:val**2 for key,val in simple_dict.items()}
my_dict2 = {key:val**2 for key,val in simple_dict.items() if val%2==0}
my_dict3 = {num:num*2 for num in [1, 2, 3]}

print(my_dict1)
print(my_dict2)
print(my_dict3)
