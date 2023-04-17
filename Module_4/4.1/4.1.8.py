socks, days = map(int, input().split())
day = 0
while socks > 0:
    socks -= 1
    day += 1
    if day % days == 0:
        socks += 1
print(day)
