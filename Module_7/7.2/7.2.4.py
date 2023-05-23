def print_initials(name, surname, middlename):
    print(f'{surname.title()} {name[0].upper()}.{middlename[0].upper()}.')
    pass

# считываем данные
name = input()
surname = input()
middlename = input()

# вызываем функцию
print_initials(name, surname, middlename)