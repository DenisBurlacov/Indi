def summa_n(t):
    s = 0
    for i in range(0, t + 1):
        s += i
    print(f'Я знаю, что сумма чисел от 1 до {t} равна {s}')


summa_n(5)
