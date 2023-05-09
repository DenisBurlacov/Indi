# a = [
#     ("Sidorov", 1995),
#     ("Lukov", 2002),
#     ("Petrov", 1991),
#     ("Gorbachev", 1984),
#     ("Kostin", 2000),
#     ("Isaev", 2005),
#     ("Eliseev", 1999),
#     ("Kozlov", 2004),
#     ("Bukov", 1995),
#     ("Gavrilov", 1980),
#     ("Efremov", 2006),
# ]
#
# b = [elem[0] for elem in a if elem[1] > 2000]
# print(b)


a = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
}


b = [a[elem] for elem in a]
print(b)