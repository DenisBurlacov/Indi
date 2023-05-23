# import turtle
#
#
# def move(a):
#     turtle.forward(a)
#     turtle.left(90)
#
#
# def draw_square(a):
#     for i in range(4):
#         move(a)
#
#
# turtle.speed(1)
#
# draw_square(60)
# turtle.goto(150, 150)
# draw_square(120)

def summa(a, b):
    return a + b


_test1 = [1, 2]
_test2 = [1, 2, 3]
_test3 = summa(_test1, _test2)
print(summa(_test1, _test2))
print(_test3)