"""
Задача 2. Финансовый отчёт

Что нужно сделать

Васе пришло очередное задание — автоматизация финансовой отчётности. Звучит сложно, а на деле нужно просто написать код,
 который будет считать нужные для отчёта вычисления автоматически. Вычисления, которые нужно реализовать в программе:
  сумму дохода первых двух кварталов поделить на сумму последних двух кварталов,
  чтобы понять динамику роста или падения дохода.

Алгоритм действий в программе:

    Запросить у пользователя четыре числа.
    Отдельно сложить два первых и два вторых.
    Разделить первую сумму на вторую.
    Вывести результат на экран.
"""
fst_quarter = int(input('Введите доход за первый квартрал: '))
snd_quarter = int(input('Введите доход за второй квартрал: '))
trd_quarter = int(input('Введите доход за третий квартрал: '))
fth_quarter = int(input('Введите доход за четвертый квартрал: '))

res = (fst_quarter + snd_quarter) / (trd_quarter + fth_quarter)
print(res)

