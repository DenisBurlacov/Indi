a = list(map(int, input().split()))
b = []
for i in a:
    if i > 0:
        b.append(i)
if len(b) != 0:
    print(min(b))
else:
    print('Empty')