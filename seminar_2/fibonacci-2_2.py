# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

n = int(input("Введите число: "))
prev = 0
next = 1
order = 2 # сразу начинаем с двойки

while next <= n:
    if next == n:
        print(order)
        break
    prev, next = next, prev + next
    order += 1
else:
    print(-1)