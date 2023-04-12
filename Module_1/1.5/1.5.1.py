# a, b = input().split()
# print(f'{a} {b}')
# a, b, c = map(int, input().split())
# print(f'{a} {b} {c}')

# year = int(input())
# print(year + 1)
#
# num = int(input())
# print(num * 2)
# print(num / 2)
#
# lenght = float(input())
# print(lenght ** 2)
#
# a, b = int(input()), int(input()),
# print(a + b)
#
# a, b = float(input()), float(input())
# s = a * b
# p = 2 * (a + b)
# print(s, p)
#
# f = float(input())
# c = (f - 32) * 5 // 9
# print(c)
# a, b = int(input()), int(input())
# print(abs(a) + abs(b))

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
i = int(input())
hours_second_1 = a * 3600
min_second_1 = b * 60
hours_second_2 = d * 3600
min_second_2 = e * 60
print((hours_second_2 + min_second_2 + i) - (hours_second_1 + min_second_1 + c))