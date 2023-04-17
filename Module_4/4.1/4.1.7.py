x, y = map(int, input().split())
days = 1
while x <= y:
    x = x * 1.15
    days += 1
print(days)