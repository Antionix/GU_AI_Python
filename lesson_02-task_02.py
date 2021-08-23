"""
Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
input().
"""

list_data = []
while True:
    x = int(input("Введите число от 0 до 99 (для прекращения введите -1):"))
    if x >= 0:
        list_data.append(x)
    else:
        break
print(list_data)
# list_data = [3, 45, 67, 23, 22, 66, 88, 3, 66, 3]
print('-'*30)

# Вариант 1
res_list_data = []
for x in range(int(len(list_data) / 2)):
    y = list_data[x * 2:x * 2 + 2]
    y.reverse()
    res_list_data.append(y)
res_list_data.append(list_data[-1:] if len(list_data) % 2 != 0 else [])
res_list_data = sum(res_list_data, [])
print(list_data)
print(res_list_data)
print('-'*30)

# Вариант 2
print(list_data)
if len(list_data) % 2 != 0:
    list_data[1:-1:2], list_data[:-1:2] = list_data[:-1:2], list_data[1:-1:2]
else:
    list_data[1::2], list_data[::2] = list_data[::2], list_data[1::2]
print(list_data)
