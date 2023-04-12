num = int(input())
previous_num = num - 1
next_num = num + 1
text_previous = "Для числа {0} предыдущим будет число {1}.".format(num, previous_num)
text_next_num = "Для числа {0} следующим будет число {1}.".format(num, next_num)
print(text_previous)
print(text_next_num)