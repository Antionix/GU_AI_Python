"""
Реализуйте базовый класс Car.
 
- у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go,
  stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
- опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
- добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
- для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
  и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
 
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""
import random


class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False

    def __init__(self, name, color, is_police):
        self.name = name
        self.color = color
        self.speed = 0
        self.is_police = is_police

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def is_police(self):
        return self.is_police

    def set_speed(self, speed):
        self.speed = speed

    def go(self, speed):
        self.speed = speed
        print(f"Машина {self.name} {self.color} цвета поехала со скоростью {self.speed} км/ч")

    def stop(self):
        print(f"Машина {self.name} {self.color} цвета остановилась")

    def turn(self, direction):
        if direction == 1:
            print(f"Машина {self.name} {self.color} цвета повернула на право")
        elif direction == 2:
            print(f"Машина {self.name} {self.color} цвета повернула на лево")
        else:
            print(f"Машина {self.name} {self.color} цвета едет прямо")

    def show_speed(self):
        print(f"Машина {self.name} {self.color} цвета едет со скоростью {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Машина {self.name} {self.color} цвета превысила скорость")
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Машина {self.name} {self.color} цвета превысила скорость")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color, True)


myCar1 = TownCar("Volvo", "желтого")
myCar2 = WorkCar("Reno", "белого")
myCar3 = SportCar("Porshe", "красного")
myCar4 = PoliceCar("Ford", "сине-желтого")

myCar1.go(random.randint(20, 80))
myCar2.go(random.randint(20, 80))
myCar3.go(random.randint(20, 80))
myCar4.go(random.randint(20, 80))

for _ in range(random.randint(4, 10)):
    myCar1.set_speed(random.randint(20, 80))
    myCar1.turn(random.randint(0, 2))
    myCar1.show_speed()

    myCar2.set_speed(random.randint(20, 80))
    myCar2.turn(random.randint(0, 2))
    myCar2.show_speed()

    myCar3.set_speed(random.randint(20, 80))
    myCar3.turn(random.randint(0, 2))
    myCar3.show_speed()

    myCar4.set_speed(random.randint(20, 80))
    myCar4.turn(random.randint(0, 2))
    myCar4.show_speed()

myCar1.stop()
myCar2.stop()
myCar3.stop()
myCar4.stop()
