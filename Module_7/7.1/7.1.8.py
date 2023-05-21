def count_letters(_str):
    count_lover = 0
    count_upper = 0
    for i in _str:
        if i.isupper():
            count_upper += 1
        if i.islower():
            count_lover += 1
    print(f'Количество заглавных символов: {count_upper}')
    print(f'Количество строчных символов: {count_lover}')


count_letters('Привет, Старина')
