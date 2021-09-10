"""
Реализовать класс Road (дорога).
 
- определить атрибуты: length (длина), width (ширина);
- значения атрибутов должны передаваться при создании экземпляра класса;
- атрибуты сделать защищёнными;
- определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
- использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной
  в 1 см*число см толщины полотна;
- проверить работу метода.
 
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def mass_of_asphalt(self, mass, blade):
        return round(self._length * self._width * mass * blade / 1000, 3)


my_road = Road(length=float(input("Введите длину дороги (м): ")),
               width=float(input("Введите ширину дороги (м): ")))

m2_asphalt = float(input("Введите массу асфальта для покрытия одного кв м (кг): "))
blade_asphalt = float(input("Введите толщину асфальтого покрытия (см): "))

print(
    f"""
Для покрытия всей дороги (ширина дороги {my_road.get_width()} м., длина дороги {my_road.get_length()} м.), 
асфальтом толщиной {blade_asphalt} см, 
понадобится {my_road.mass_of_asphalt(mass=m2_asphalt, blade=blade_asphalt)} т. асфальта
""")
