x = input()
y = input()
strings = " abcdefgh"
x1, x2 = x[0], int(x[1])
y1, y2 = y[0], int(y[1])
x1 = strings.find(x1)
y1 = strings.find(y1)
if (x1 + x2) % 2 == 0 and (y1 + y2) % 2 == 0 or (x1 + x2) % 2 != 0 and (y1 + y2) % 2 != 0:
    print("YES")
else:
    print("NO")


