# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#    Используйте форматирование строк.
step = 3
while True:
    seconds = int(input("Введите количество секунд: "))
    if step == 0:
        print("Попытки закончились")
        break

    if seconds < 0:
        step = step - 1
        print("Введено неверное количество секунд. Попробуйте снова, осталось попыток: {} ".format(step))
    else:
        hour = seconds // 3600 % 24
        seconds = seconds % 3600
        minute = seconds // 60
        seconds = seconds % 60
        print("Введенное количество секунд соответствует {0:02}:{1:02}:{2:02}".format(hour, minute, seconds))
        break


