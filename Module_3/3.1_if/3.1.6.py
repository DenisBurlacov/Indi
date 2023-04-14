
# if number := int(input("Enter the value")) == 100:
#     print("one hundred")
# else:
#     print("no one_hundred")

if (value := int(input())) <= 10000:
    print(f'Сумма {value} не превышает лимит, проходите')
else:
    dif = value - 10000
    print(f"Ого! {value}! Куда вам столько? Мы заберем {dif}")