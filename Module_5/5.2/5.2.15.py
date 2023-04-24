n = int(input())
for i in range(n):
    s = input()
    if len(s) > 10:
        b = s[0]
        c = s[-1]
        d = s[1: -2]
        s = b + str(len(d) + 1) + c
    print(s)