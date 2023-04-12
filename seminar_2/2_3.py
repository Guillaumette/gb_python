# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

days = int(input("Введите общее количество дней: "))
count = 0
consecutive = 0 # чтобы посчитать именно подряд

for i in range(days):
    day = int(input(f'{i + 1} день: '))

    if day > 0:
        count += 1
        if count > day: # на случай, если снова будет минусовая температура
            consecutive = count
    else:
        count = 0

print(f'Количество дней, идущих подряд, со средней температурой больше 0 градусов - {consecutive}')
