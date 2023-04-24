n = int(input())
a = []
for i in range(n):
    s = input().lower()
    if 'соль' not in s:
        a.append(s)
print(', '.join(a))
