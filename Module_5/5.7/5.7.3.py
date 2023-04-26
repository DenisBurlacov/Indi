n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for j in range(n - 1, -1, -1):
    for i in range(n - 1, -1, -1):
        print(a[i][j], end=' ')
    print()