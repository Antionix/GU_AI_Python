"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
(2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
import random
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_on_clothes(self):
        pass


class Coat(Clothes):
    size_coat = 0

    def __init__(self, size):
        self.size_coat = size

    def __str__(self):
        return f"Пальто {self.size_coat} размера (требуется {self.fabric_on_clothes} м2 ткани)"

    @property
    def fabric_on_clothes(self):
        return round(self.size_coat / 6.6 + 0.5, 2)


class Costume(Clothes):
    height = 0

    def __init__(self, size):
        self.height = size

    def __str__(self):
        return f"Костюм {self.height} роста (требуется {self.fabric_on_clothes} м2 ткани)"

    @property
    def fabric_on_clothes(self):
        return round(2 * self.height + 0.3, 2)


clothes = []

for _ in range(random.randint(5, 10)):
    if random.randint(1, 9) % 2 == 0:
        clothes.append(Coat(random.randint(25, 46)))
    else:
        clothes.append(Costume(random.randint(5, 12)))

all_fabric_on_clothes = 0
for i in clothes:
    all_fabric_on_clothes += i.fabric_on_clothes
    print(i)

print(f"{'-'*80}\n Всего потребуется: {all_fabric_on_clothes} м2 ткани")
