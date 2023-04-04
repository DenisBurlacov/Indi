import math
a, b, c = map(int, input().split())
s = (((a + b) * 2) * c) / 16
print(math.ceil(s))