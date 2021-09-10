"""
Реализовать класс Stationery (канцелярская принадлежность).
 
- определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
- создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
- в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
- создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = ""
    color = ""

    def __init__(self, title, color):
        self.title = title
        self.color = color

    def draw():
        print("Запуск отрисовки»")


class Pen(Stationery):
    def __init__(self, color):
        super().__init__("ручка", color)

    def draw(self):
        print(f"{self.title} пишет чернилами (цвет {self.color})")


class Pencil(Stationery):
    def __init__(self, color):
        super().__init__("карандащ", color)

    def draw(self):
        print(f"{self.title} рисует (цвет {self.color})")


class Handle(Stationery):
    def __init__(self, color):
        super().__init__("маркер", color)

    def draw(self):
        print(f"{self.title} отмечает текст (цвет {self.color})")


myPen = Pen("черный")
myPencil = Pencil("зеленый")
myHandle = Handle("желтый")

myPen.draw()
myPencil.draw()
myHandle.draw()
