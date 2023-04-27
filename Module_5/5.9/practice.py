# a = [1 for i in range(7)]
# print(a)
#
# a = [i + 1 for i in range(10) if i % 2 == 0]
# print(a)
#
# a = [i % 4 for i in range(1, 15)]
# print(a)
#
# a = [i for i in 'Hello']
# print(a)
#
# b = [i * 5 for i in 'hellos']
# print(b)
#
# a = [ord(i) for i in 'abcdef']
# print(a)
# import time
# start = time.time()
# a = []
# for i in [2, 3, 4, 5]:
#     for j in [1, 2, 3]:
#         if i * j >= 10:
#             a.append(i * j)
# print(a)
# end = time.time() - start
# print(end)
#
#
#
#
# start_second = time.time()
# b = [i * j for i in [2, 3, 4, 5] for j in [1, 2, 3] if i * j >= 10]
# print(b)
# end_second = time.time() - start_second
# print(end_second)
#
# if end > end_second:
#     print(end)

n = 3
m = 4
a = [[0] * m for i in range(n)]
a[1][2] = 100
print(a)
print('--/--/' * 12)
for i in a:
    print(i)

