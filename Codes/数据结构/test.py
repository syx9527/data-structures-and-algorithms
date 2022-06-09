import copy

c = [1, 2, 3]
a = 1
b = copy.deepcopy(a)
print("a", id(a))
print("b", id(b))
print("c", id(c))
print("c[1]", id(c[1]))
print(a == b if a == b else a == 1)
