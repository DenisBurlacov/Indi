n = int(input())
i = 1
# while i <= n // 2:
#     if n % i == 0:
#         print(i, end=' ')
#     i += 1
# print(n)
a = []
while i * i <= n:
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)
    i += 1
a.sort()
print(a)
