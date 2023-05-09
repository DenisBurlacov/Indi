# a = [i ** 2 for i in range(1, 11)]
# print(a)
#
# dect = {i: i ** 2 for i in range(1, 11)}
# print(dect)
#
# word_dict = {word: len(word) for word in ["hello", "hi", "www"]}
# print(word_dict)
#
# data = {
#     "Джеф Безос" : '177',
#     "Илон Маск": '126',
#     "бернард Арно": 150,
#     "БиЛл ГейтС": '124'
# }

# new_data = {key.title(): int(value) for key, value in data.items()}
# print(data)
# print(new_data)

users = [
    [0, "Bob", "password"],
    [1, "code", "python"],
    [2, "Stack", "overflow"],
    [3, "username", "1234"],
]

new_users = {users[0]: user for user in users}
print(new_users[1])