s = list(input().lower())
a = []
for i in s:
    a.append(s.count(i))
print(max(a))