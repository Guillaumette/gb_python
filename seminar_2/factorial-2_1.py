# Найти факториал N через while.

n = int(input("Введите неотрицательное число: "))
i = 1
f = 1

if n < 0:
    print("Введено некорректное значение")
elif  n == 0 or n == 1:
    print(f'{n}! = 1')
else:
    while i <= n:
        f *= i
        i += 1
    print(f'{n}! = {f}')