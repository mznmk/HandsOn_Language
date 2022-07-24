from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7]
s = "my name is tokugawa ieyasu"
print(Counter(li))
print(Counter(s))

dd = defaultdict(lambda: "does not exist", {"a": 1, "b": 2})
print(dd["a"])
print(dd["c"])

od1 = OrderedDict()
od1["a"] = 1
od1["b"] = 2
od1["c"] = 3
od2 = OrderedDict()
od2["c"] = 3
od2["b"] = 2
od2["a"] = 1
print(od1 == od2)
