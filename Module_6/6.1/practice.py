print(None)
print(type(None))

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a), id(b))
print('---/' * 6)
c = None
d = None
print(id(c), id(d))
print(c == d, c is d)