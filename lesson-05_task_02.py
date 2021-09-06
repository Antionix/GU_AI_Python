"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""
lines_in_file = 0
with open("src_task_01-02.txt", "r", encoding="utf-8") as f:
    for s in f.readlines():
        lines_in_file += 1
        words_in_line = len(s.split())
        print(f"Строка {lines_in_file} = {words_in_line} слов")

print(f"В файле {lines_in_file} строк")

