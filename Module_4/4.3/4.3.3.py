x = int(input())
max_num = 0
min_num = 9
while x > 0:
    last_num = x % 10
    if last_num > max_num:
        max_num = last_num
    if last_num < min_num:
        min_num = last_num
    x = x // 10
print(min_num)
print(max_num)