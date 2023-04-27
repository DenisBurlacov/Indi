n = int(input())
triangle = []

for i in range(n + 1):
    triangle.append([1] + [0] * n)

for i in triangle:
    print(i)