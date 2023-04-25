a = list(map(int, input().split()))
search_value = int(input())
len_list = len(a)
result = 0
for i in range(len_list):
    if search_value == a[i]:
        result = i + 1
        break
    else:
        result = 'ErrorValue'
print(result)