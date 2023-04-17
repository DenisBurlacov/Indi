a, b = map(int, input().split())
hour = 0
burn = 0
while a > 0:
    a -= 1
    hour += 1
    burn += 1
    if burn % b == 0:
        a += 1
        burn = 0
print(hour)
