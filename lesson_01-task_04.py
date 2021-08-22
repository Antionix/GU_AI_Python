# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#    Для решения используйте цикл while и арифметические операции.
step = 5
while True:

    if step==0:
        print("Попытки закончились")
        break

    user_number = int(input("Введите целое положительное число: "))
    input_number = user_number

    if user_number < 0:
        step -= 1
        print(f"Введено отрицательное число, попробуйте снова. Осталось попыток: {step}")
    else:
        max_number = 0
        while user_number > 0:
            current_number = user_number % 10
            user_number = user_number // 10
            if current_number > max_number:
                max_number = current_number
        print(f"Самая большая цифра в числе {input_number} = {max_number}")
        break
