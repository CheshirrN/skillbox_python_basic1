"""
Задача 5. Модуль числа

Что нужно сделать

Создайте программу, которая найдёт модуль очередного числа x. Если число x отрицательное,
то она должна перевести его в положительное, а в конце на экране должен быть модуль введённого числа.


Пример:

Ввели 5, ответ 5

Ввели −7, ответ 7

Подсказка: в некоторых случаях достаточно переприсвоить переменную со знаком минус.
"""
num = int(input('Введите число: '))
if num < 0:
    num2 = -1 * num
else:
    num2 = num
print(f'ввели {num}, ответ {num2}')