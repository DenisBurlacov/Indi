num = int(input())
hours = (num // 3600) % 24
num %= 3600
minute = num // 60
num %= 60
sec = num
print(hours, ":", minute // 10, minute % 10, ":", sec // 10, sec % 10, sep='')