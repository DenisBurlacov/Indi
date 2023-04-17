n = int(input())
level = 0
coub_lever = 0
s = 0
while s < n:
    level += 1
    coub_lever += level
    s += coub_lever
if s == n:
    print(level)
else:
    print(level - 1)


