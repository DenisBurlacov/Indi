a, b = map(int, input().split())
z = a * b
while b > 0:
    a, b = b, a % b
print(int(z / a))