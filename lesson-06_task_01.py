"""
Создать класс TrafficLight (светофор).
 
- определить у него один атрибут color (цвет) и метод running (запуск);
- атрибут реализовать как приватный;
- в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
- продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
  третьего (зелёный) — на ваше усмотрение;
- переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
- проверить работу примера, создав экземпляр и вызвав описанный метод.
 
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""
import random
from itertools import cycle

TIME_COLOR = {"Красный": 7, "Желтый": 2, "Зеленый": 6}


class TrafficLight:
    __color = ""

    def __init__(self, start_color):
        self.__color = start_color

    def get_color(self):
        return self.__color

    def set_color(self, set_color):
        self.__color = set_color

    def running(self):
        status = 0
        life_cycle = random.randint(10, 25)

        for c in cycle(["Красный", "Желтый", "Зеленый"]):
            if status == 0:
                if self.__color == c:
                    status = 1
                else:
                    continue

            self.set_color(c)
            print("-" * 60)
            print(f"Светофор: горит {self.get_color()}")

            for t in range(TIME_COLOR[self.__color]):
                print(f"  ... ({t + 1} сек.)")

            if life_cycle == 0:
                print("Светофор сломался ...")
                break
            else:
                life_cycle -= 1


print(TIME_COLOR)

my_Traffic_Light = TrafficLight(list(TIME_COLOR.keys())[random.randint(0, 99) % 3])
print(f"Светофор включен, текущий цвет: {my_Traffic_Light.get_color()}")

my_Traffic_Light.running()
