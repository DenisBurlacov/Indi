# n, m = map(int, (input().split()))
# a = []
# b = []
#
# for i in range(n):
#     l = list(map(int, input().split()))
#     a.append(l)
# for i in range(n):
#     s = 0
#     for j in range(m):
#         s += a[i][j]
#     b.append()
#
# print(max(b))
# print(b.index(max(b)))

n, m = map(int, input().split())  # n-кол-во строк, m-столбцов
a = []  # пустой список для ввода
c = []  # пустой список для сумм

for i in range(n):
    l = list(map(int, input().split()))  # Заполнение списка цифрами через пробел
    a.append(l)  # Добавление вложенного списка во внешний список
for i in range(n):  # цикл по строкам
    s = 0  # переменная для суммы строки
    for j in range(m):  # цикл по толбцам
        s += a[i][j]  # складываем все столбцы в строке
    c.append(s)  # Добавление сумму строки в список

print(max(c))  # вывод максимального значения в списке с
print(c.index(max(c)))