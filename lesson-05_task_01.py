"""
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

with open("src_task_01.txt", "w", encoding="utf-8") as f:
    while True:
        str_source = input('Введите текст (завершите ввод пустой строкой:')
        if len(str_source) == 0:
            break
        # f.writelines(f"{str_source}")
        print(str_source, file=f)
