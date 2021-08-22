# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
#    Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
user_number = input("Введите число от 1 до 9: ")
if len(user_number) != 1:
    print("Введено не правильное число")
else:
    print("Сумма чисел n + nn + nnn для {} = {} = {}".format(user_number,
                                                             "{} + {} + {}".format(user_number, user_number*2, user_number*3),
                                                             int(user_number) + int(user_number*2) + int(user_number*3)))

