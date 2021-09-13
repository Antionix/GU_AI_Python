"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
(__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно
....
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""
import random


class Cells:
    number_of_cells = 0

    def __init__(self, number_cell):
        self.number_of_cells = number_cell

    # Сложение. Объединение двух клеток.
    # При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
    def __add__(self, other):
        return Cells(self.number_of_cells + other.number_of_cells)

    # Вычитание. Участвуют две клетки.
    # Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
    # нуля, иначе выводить соответствующее сообщение.
    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return Cells(self.number_of_cells - other.number_of_cells)
        else:
            return f"Нельзя из меньшей клетки ({self.number_of_cells}) вычесть большую клетку ({other.number_of_cells})"

    # Умножение. Создается общая клетка из двух.
    # Число ячеек общей клетки определяется как произведение количества ячеек этих
    # двух клеток.
    def __mul__(self, other):
        return Cells(self.number_of_cells * other.number_of_cells)

    # Деление. Создается общая клетка из двух.
    # Число ячеек общей клетки определяется как целочисленное деление количества
    # ячеек этих двух клеток.
    def __truediv__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return Cells(self.number_of_cells // other.number_of_cells)
        else:
            return f"Нельзя делить меньшую клетку ({self.number_of_cells}) на большую клетку ({other.number_of_cells})"

    def make_order(self, number_cell_in_row):
        src = "--" * number_cell_in_row + f" ({number_cell_in_row})\n"
        for _ in range(self.number_of_cells // number_cell_in_row):
            src += "# " * number_cell_in_row + "\n"
        src += "# " * (self.number_of_cells % number_cell_in_row) + "\n" * (
            0 if self.number_of_cells % number_cell_in_row == 0 else 1)
        src += "--" * number_cell_in_row + "\n"
        return src

    def __str__(self):
        return self.make_order(10)


cell1 = Cells(random.randint(3, 15))
cell2 = Cells(random.randint(3, 15))
cell3 = Cells(random.randint(3, 15))
cell4 = Cells(random.randint(3, 15))

cell1_add_cell2 = cell1 + cell2
cell2_sub_cell3 = cell2 - cell3
cell3_mul_cell4 = cell3 * cell4
cell4_div_cell1 = cell4 / cell1

print(f"cell1\n{cell1.make_order(random.randint(3, 9))}")
print(f"cell2\n{cell2.make_order(random.randint(3, 9))}")
print(f"cell3\n{cell3.make_order(random.randint(3, 9))}")
print(f"cell4\n{cell4.make_order(random.randint(3, 9))}")

print(f"cell1_add_cell2\n{cell1_add_cell2}")
print(f"cell2_sub_cell3\n{cell2_sub_cell3}")
print(f"cell3_mul_cell4\n{cell3_mul_cell4}")
print(f"cell4_div_cell1\n{cell4_div_cell1}")
