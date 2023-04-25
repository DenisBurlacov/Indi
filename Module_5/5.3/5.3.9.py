s = input()
sum = 0
count = 0
for i in s:
    if '0' <= i <= '9':
        sum += int(i)
        count += 1
print(count, sum)
