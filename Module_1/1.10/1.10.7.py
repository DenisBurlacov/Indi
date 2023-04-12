num_1, num_2 = map(int, input().split())
num_1 %= 7
num_2 %= 7
print(num_1 == 0 and num_2 == 0)