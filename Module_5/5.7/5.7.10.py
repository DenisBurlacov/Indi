n, m = map(int, input().split())
a = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

max = 0
i_max = 0
j_max = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > max:
            max = a[i][j]
            i_max = i
            j_max = j
print(max)
print(i_max, j_max)

