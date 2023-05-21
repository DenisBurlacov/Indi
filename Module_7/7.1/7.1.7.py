
# Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.
#
# Сложным паролем будет считаться комбинация символов, в которой :
#
# Есть хотя бы 3 цифры
# Есть хотя бы одна заглавная буква
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов
# Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"
#
# Вам необходимо написать только определение функции check_password


def check_password(password):
    count_digit = 0
    count_upper = 0
    count_spec = 0
    for s in password:
        if s.isdigit():
            count_digit += 1

        if s.isupper():
            count_upper += 1

        if s in "!@#$%*":
            count_spec += 1

    if count_digit >= 3 and count_upper > 0 and count_spec > 0 and len(password) >= 10:
        print("Perfect password")
    else:
        print("Easy peasy")


check_password('1234')
check_password('adlskfj')
check_password('aasdf123')
