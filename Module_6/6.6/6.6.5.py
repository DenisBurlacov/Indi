list_int = list(map(int, input().split()))

dic = {}
x = len(list_int) - 1

while x != 0:
    if len(dic) == 0:
        dic = {list_int[x - 1] : list_int[x]}
    else:
        dic = {list_int[x - 1] : dic}
    x -= 1
print(dic)