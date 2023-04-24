# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

lst = []
for i in range(1, int(input("Введите верхнюю граниу длины списка: "))):
    lst.append(randint(1, 10))
print(*lst)

x = int(input("Введите число X: "))

found = lst[0] # найденное значение (первоначально первое)
for i in lst:
    if abs(i - x) < abs(found - x):
        found = i

print(found)