a = [[0, 2, 4, 6],
     [1, 5, 9, 13],
     [3, 10, 17, 19]]
for i in range(3):
    s = 0
    for j in range(4):
        s += a[i][j]
        # print(a[i][j], end=' ')
    print(s)