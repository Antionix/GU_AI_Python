"""
Реализовать два небольших скрипта:
- итератор, генерирующий целые числа, начиная с указанного;
- итератор, повторяющий элементы некоторого списка, определённого заранее.

Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый
цикл не должен быть бесконечным. Предусмотрите условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""
from itertools import count
from itertools import cycle


def my_iter1(n, k=25):
    for i in count(n):
        if i > k:
            break
        else:
            yield round(i)


def my_iter2(in_list, k=5):
    c = 0
    for item in cycle(in_list):
        if c > len(in_list) * k:
            break
        else:
            yield item
            c += 1


print([x for x in my_iter1(6)])
print([x for x in my_iter1(3.3)])
print([x for x in my_iter1(5.6, 10)])

print([x for x in my_iter2("Hello world!")])
print([x for x in my_iter2("Hello world!", 2)])
