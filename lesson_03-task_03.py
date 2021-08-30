"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму
наибольших двух аргументов.
"""


def my_func1(x1, x2, x3):
    try:
        if x1 > x2:
            return x1 + x2 if x2 > x3 else x1 + x3
        else:
            return x1 + x2 if x1 > x3 else x2 + x3
    except TypeError as error:
        print(error)


def my_func2(x1, x2, x3):
    try:
        list_val = sorted([x1, x2, x3])
        list_val = list_val[1:]
        return sum(list_val)
    except (IndentationError, TypeError) as err:
        print(err)


print(my_func1(2, 6, 'f'))
print(my_func1(2, 6, 4))
print(my_func1(5, 6, 2))

print(my_func2(2, 6, 'f'))
print(my_func2(2, 6, 4))
print(my_func2(5, 6, 2))

