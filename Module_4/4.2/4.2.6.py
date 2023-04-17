a, b = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
l3 = l1 + l2
result = []
while len(l3) != 0:
    a = min(l3)
    result.append(a)
    list.remove(a)
print(*result)
