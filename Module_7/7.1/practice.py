def check_even(a):
    if a % 2 == 0:
        print(a, 'chetnoe')
    else:
        print(a, 'nechetnot')


for number in range(20, 31):
    check_even(number)
print('*' * 25)
print()


# ============================================================================

def factorial(n):
    pr = 1
    for i in range(2, n + 1):
        pr *= i
    print(f'factorial {n} = {pr}')


factorial(3)
factorial(5)
factorial(10)
print('*' * 25)
print()
# ==============================================================================
# Ещё один вариант определения и вызова функции:

if 5 > 1:
    def print_hello():
        print('hello')
else:
    def print_hello():
        print('HELLO')

print_hello()