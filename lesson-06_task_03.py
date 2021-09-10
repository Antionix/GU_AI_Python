"""
Реализовать базовый класс Worker (работник).
 
- определить атрибуты: name, surname, position (должность), income (доход);
- последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
  например, {"wage": wage, "bonus": bonus};
- создать класс Position (должность) на базе класса Worker;
- в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом
  премии (get_total_income);
- проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
  значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    name = ""
    surname = ""
    position = ""
    income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income["wage"] = wage
        self.income["bonus"] = bonus

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_position(self):
        return self.position

    def get_income(self):
        return self.income

    def set_position(self, position):
        self.position = position

    def set_income_wage(self, wage):
        self.income["wage"] = wage

    def set_income_bonus(self, bonus):
        self.income["bonus"] = bonus


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]


person = Position("Ivan", "Petrov", "manager", 2000, 500)

print(person.get_full_name())
print(person.get_total_income())
print(person.get_position())
