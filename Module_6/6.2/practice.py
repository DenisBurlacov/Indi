# variants for creating tuple
a = 1, 2, 3, 4, 5
b = tuple(range(1, 5))
c = ()
d = tuple([1, 2, 3])
e = tuple('abcdef')

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print('---/' * 13)

print(len(a))
print(2 in a)
print(a + b)
print(a * 2)
print('min =', min(a), 'max =', max(a), 'sum =', sum(a))
print(a[1])
a = 1, 'Hello', 3, [10, 20, 30], False, 5
a[3].append(100)

print(a[3])
print(a)

