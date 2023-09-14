"""
Задание 5. Наибольшая сумма цифр
Что нужно сделать

Пользователь вводит N чисел. Среди натуральных чисел, которые он указал, найдите наибольшее по сумме цифр.
Выведите на экран это число и сумму его цифр.
"""
while True:
    try:
        am_num = int(input('Введите количество чисел: '))
        break
    except ValueError:
        print('Некорректный ввод. Пожалуйста введите число.')

lst = []
for num in range(am_num):
    while True:
        try:
            ent_num = int(input(f'Введите {num + 1} число: '))
            break
        except ValueError:
            print('Некорректный ввод. Пожалуйста введите число.')
    lst.append(ent_num)

max_len = 0
max_num = 0
for list_num in lst:
    if (len(str(list_num)) >= max_len) and (max_num < int(list_num)):
        max_len = len(str(list_num))
        max_num = int(list_num)

print(f'Самое большое число в последовательности: {max_num}. Состоит из {max_len} цифр.')
