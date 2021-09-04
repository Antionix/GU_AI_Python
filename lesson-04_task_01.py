"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных
значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def print_help():
    print(
        """
        Для выполнеия расчета звпустить скрипт командой
        lesson-04_task-01.py work_hours cost_hour bonus
        где:
          lesson-04_task-01.py  - имя скрипта 
          work_hours            - выработка в часах
          cost_hour             - ставка в час
          bonus                 - премия

        *все параметры обязательны          
        """
    )


def zp_calc(hours, cost, bonus=0):
    return round(float(hours) * float(cost) + float(bonus), 2)


# print(argv, len(argv))

if len(argv) == 4:
    pg_name, current_work_hours, current_cost_hour, current_bonus = argv
    print(
        f"при выработке: {current_work_hours} ч., по ставке: {current_cost_hour} руб в час, c премией {current_bonus} руб.")
    # sum_zp = zp_calc(current_work_hours, current_cost_hour, current_bonus)
    print(f"ващ заработок составит {zp_calc(current_work_hours, current_cost_hour, current_bonus):.2f} руб.")
else:
    print('Неправильый вызов функции!!!')
    print_help()
