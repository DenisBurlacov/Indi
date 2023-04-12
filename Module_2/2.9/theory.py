gender = {
    'm': 'Дорогой',
    'f': 'Дорогая'
}

a = [
    ['Семён', 'Семёнов', 32.56, 'm'],
    ['Зоя', 'Иванова', 50, 'f'],
    ['Катерина', 'Петровна', 567, 'f']
]

for name, mid_name, balance, g in a:
    text = f"{gender[g]} {name} {mid_name}, баланс Вашего лицевого счета составляет {balance} грн."
    print(text)