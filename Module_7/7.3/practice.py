def even(x):
    return x % 2 == 0


for i in range(1, 11):
    print(i, even(i))


def factorial(x):
    pr = 1
    for i in range(2, x + 1):
        pr = pr * i
    return pr


for i in range(1, 8):
    print(i, factorial(i))
