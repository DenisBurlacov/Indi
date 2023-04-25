n = int(input())
a = list(map(int, input().split()))
count = 0
for run in range(n - 1):
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            count += 1
            a[i], a[i + 1] = a[i + 1], a[i]
for i in a:
    print(i, end=' ')
print()
print(count)

