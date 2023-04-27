n = int(input())
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            b.append(a[i][j])
print(max(b))