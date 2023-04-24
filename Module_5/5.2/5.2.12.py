from random import randint
mishka_result = 0
kris_result = 0
n = int(input())
for i in range(n):
    mishka_attemp, kris_attemp = map(int, input().split())
    if mishka_attemp == kris_attemp:
        mishka_result += 1
        kris_result += 1
    elif mishka_attemp > kris_attemp:
        mishka_result += 1
    else:
        kris_result += 1
if mishka_result > kris_result:
    print('Mishka')
elif kris_result > mishka_result:
    print('Chris')
else:
    print('Friendship is magic!^^')
