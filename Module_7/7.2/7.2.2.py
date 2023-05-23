# объявление функции
def is_between(name, surname, middlename):
    if surname <= name <= middlename or surname >= name >= middlename:
        print(True)
    else:
        print(False)
    pass

# считываем данные
a, b, c = map(int, input().split())

# вызываем функцию
is_between(a, b, c)