"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
...
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""
import random


class Matrix:
    matrix = []
    __dimension = []

    def __init__(self, matrix_list):
        d = 0
        for x in matrix_list:
            d = len(x) if d == 0 or d == len(x) else -1
        if d > 0:
            self.matrix = matrix_list
            self.__dimension = [len(matrix_list), d]
        else:
            print("Неверные данные для инициализации")

    def get_dimension(self):
        return self.__dimension

    def __str__(self):
        mm = F"Matrix {self.__dimension[0]}x{self.__dimension[1]}\n{'-' * self.__dimension[0] * 6}\n"
        for x in self.matrix:
            for y in x:
                mm += f"{y:6}"
            mm += "\n"
        return mm

    def __add__(self, other):
        m_add = []
        if self.__dimension == other.get_dimension():
            for x in range(self.__dimension[0]):
                r = []
                for y in range(self.__dimension[1]):
                    r.append(self.matrix[x][y] + other.matrix[x][y])
                m_add.append(r)
            return Matrix(m_add)
        else:
            print("Размер матриц разный. сложение невозможно")


my_matrix1 = Matrix([[random.randint(-50, 50), random.randint(-50, 50), random.randint(-50, 50)],
                     [random.randint(-50, 50), random.randint(-50, 50), random.randint(-50, 50)],
                     [random.randint(-50, 50), random.randint(-50, 50), random.randint(-50, 50)]])

my_matrix2 = Matrix([[random.randint(-50, 50), random.randint(-50, 50), random.randint(-50, 50)],
                     [random.randint(-50, 50), random.randint(-50, 50), random.randint(-50, 50)],
                     [random.randint(-50, 50), random.randint(-50, 50), random.randint(-50, 50)]])

print(my_matrix1)
print(my_matrix2)
print(my_matrix1 + my_matrix2)

