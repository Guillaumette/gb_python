# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

n = int(input("Введите количество элементов: "))

lst = []

for i in range(n):
    lst.append(randint(1, 10))
print(*lst)

min_n = min(lst)
max_n = max(lst)

for i in range(len(lst)):
    if lst[i] != min_n and lst[i] != max_n:
        print(i)