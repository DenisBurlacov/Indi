# длинна пароля 3
# count = 0
# from string import printable
# for b1 in printable:
#     for b2 in printable:
#         for b3 in printable:
#             count += 1
#             print(b1, b2, b3)
#
# print(count)

# for i in range(1, 10):
#     for j in range(1, 11):
#         print(f'{i} * {j} = {i * j}')
#     print()

# Сколько шестибуквенных слов, начинающихся и заканчивающихся согласной буквой
# и содержащих ровно 2 гласные можно составить из букв Т, Ы, К, В, А?
# Каждая из допустимых букв может входить в слово несколько раз.
# Эту задачу можно сделать при помощи цикла, и сразу переведём буквы в латиницу для более удобной работы.
k = 0
for b1 in 'tukva':
    for b2 in 'tukva':
        for b3 in 'tukva':
            for b4 in 'tukva':
                for b5 in 'tukva':
                    for b6 in 'tukva':
                        rez = b1 + b2 + b3 + b4 + b5 + b6
                        if rez[0] in 'tkv' and rez[-1] in 'tkv':
                            if rez.count('a') + rez.count('u') == 2:
                                print(rez)
                                k += 1
print(k)


