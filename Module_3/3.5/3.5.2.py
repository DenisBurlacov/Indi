months_num = int(input())
match months_num:
    case 2:
        print('28')
    case 4 | 6 | 9 | 11:
        print(30)
    case _:
        print(31)