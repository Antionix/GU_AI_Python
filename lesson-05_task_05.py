"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
from random import randint

all_sum = 0
with open("src_text_05.txt", "w+", encoding="utf-8") as f:
    for _ in range(randint(10, 30)):
        print(" ".join([str(randint(1, 99)) for x in range(randint(10, 20))]), file=f)
    print("Файл с данными подготовлен ..")
    f.seek(0)

    print("Вычисление суммы чисел в файле ...")
    for line in f.readlines():
        all_sum += sum([a for a in map(int, line.split())])

print(f"Сумма чисел в файле равна: {all_sum}")
