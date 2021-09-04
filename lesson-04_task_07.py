"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from functools import reduce


def multi(x1, x2):
    return x1 * x2


def pre_fact(n):
    if n == 1 or n == 0:
        # yield f'{n}!=1'
        yield 1
    else:
        for x in range(1, n + 1):
            if x == 1:
                # yield '1!=1'
                yield 1
            else:
                # yield '{}!={}'.format(x, reduce(multi, [i for i in range(1, x + 1)]))
                yield reduce(multi, [i for i in range(1, x + 1)])


def fact(n):
    for i in range(1, n + 1):
        yield [x for x in pre_fact(i)]


for el in fact(8):
    print(el)
