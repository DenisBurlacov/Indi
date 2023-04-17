n = input()
while int(n[0]) != 1 and int(n) < 10 ** 9:
    n = int(n[0]) * int(n)
    n = str(n)
print(n)