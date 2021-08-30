"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
   Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_div1(x, y):
    try:
        res = x / y if y != 0 else -1
    except TypeError as err:
        print(err)
    else:
        return res


def my_div2(x, y):
    try:
        res = x / y
    except (TypeError, ZeroDivisionError) as err:
        print(err)
    else:
        return res


print(my_div1(6, 3))
print(my_div1(4, 0))
print(my_div1('s', 0))
print(my_div1(9, '3'))

print('-' * 20)

print(my_div2(6, 3))
print(my_div2(4, 0))
print(my_div2('s', 0))
print(my_div2(9, '3'))
