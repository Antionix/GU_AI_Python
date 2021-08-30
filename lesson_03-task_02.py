"""
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""


def person(first_name, second_name, year, town, email, phone):
    """ Функция осуществляет вывод данных о пользователе одной строкой

    Принимаемые параметры:
    first_name - имя пользователя
    second_name - фамилия пользователя
    year - год рождения пользователя
    town - город проживания пользователя
    email - email пользователя
    phone - телефон пользователя
    """
    print(f"{first_name} {second_name}, {year} года рождения, проживает в {town}, e-mail:{email}, тел.:{phone}")


person("Иван", "Смирнов", 2000, "Москва", "is@mail.my", "+7 888 123-44-55")
person(
    first_name=input("Введите имя пользователя: "),
    second_name=input("Введите фамилия пользователя: "),
    year=input("Введите год рождения пользователя: "),
    town=input("Введите город проживания пользователя: "),
    email=input("Введите email пользователя: "),
    phone=input("Введите телефон пользователя: ")
)

# print(help(person))
