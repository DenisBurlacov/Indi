s = input().split()
a = []
b = []
for i in s:
    if i.lower() not in a:
        a.append(i.lower())
        b.append(i)
print(*b)