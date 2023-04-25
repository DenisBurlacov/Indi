n = int(input())
coun_num = 0
divider = 0

for i in range(n + 1, 2 * n):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            divider += 1
            break
    if divider == 0:
        coun_num += 1
    divider = 0
print(coun_num)