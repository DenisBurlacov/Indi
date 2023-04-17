# how many num in number
x = int(input())
kol = 0
kol_ch = 0
s = 0
pr = 1
maximum = 0
minimum = 9
while x > 0:
    last = x % 10
    kol += 1
    if last % 2 == 0:
        kol_ch += 1
    s += last
    pr *= last
    if last > maximum:
        maximum = last
    if last < minimum:
        minimum = last
    x = x // 10
print("total num:", kol)
print("total chet", kol_ch)
print("total summ", s)
print("proizved =", pr)
print("maxNum=", maximum)
print("minNum=", minimum)
