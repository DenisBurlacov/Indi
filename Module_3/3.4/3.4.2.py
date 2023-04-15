a, b, c = int(input()), int(input()), int(input()),
if a == b == c:
    print(3)
elif a != b != c and a != c != b and b != a != c:
    print(0)
else:
    print(2)