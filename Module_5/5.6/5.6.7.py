n, m = map(int, input().split())
coutn = 0

for a in range(n + 1):
    for b in range(m + 1):
        if a + b ** 2 == m and a ** 2 + b == n:
            coutn += 1
print(coutn)