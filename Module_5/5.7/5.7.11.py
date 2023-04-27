n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

max_score = 0
max_summa = 0
max_index = 0

for row in range(n):
    max_try = 0
    s = 0
    for column in range(m):
        s += a[row][column]
        if a[row][column] > max_try:
            max_try = a[row][column]
    if max_try > max_try:
        max_score = max_try
        max_summa = s
        max_index = row
    elif max_try == max_score and s > max_summa:
        max_score = max_try
        max_summa = s
        max_index = row
print(max_index)

n, m = map(int, input().split())
matrix = []
mx = 0
l = []

for i in range(n):
    k = list(map(int, input().split()))
    matrix.append(k)
for i in range(n):
    for j in range(m):
        if matrix[i][j] > mx:
            mx = matrix[i][j]

for i in range(n):
    if mx in matrix[i]:
        l.append(sum(matrix[i]))
    else:
        l.append(0)

print(l.index(max(l)))