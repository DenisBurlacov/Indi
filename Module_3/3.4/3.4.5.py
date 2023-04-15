a = float(input())
b = float(input())
d = input()
if b == 0 and d == '/':
    print('Неизвестно')
elif d == '+':
    print(a + b)
elif d == '-':
    print(a - b)
elif d == '*':
    print(a * b)
elif d == '/':
    print(a / b)
else:
    print('Неизвестно')