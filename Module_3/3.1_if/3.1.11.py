ticket = input().zfill(6)
if (int(ticket[0]) + int(ticket[1]) + int(ticket[2])) == \
        (int(ticket[3]) + int(ticket[4]) + int(ticket[5])):
    print("YES")
else:
    print("NO")