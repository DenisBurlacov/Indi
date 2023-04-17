num = int(input())
count = 0
while num > 0:
    if num % 10 == 7:
        count += 1
    num = num // 10
print(count)