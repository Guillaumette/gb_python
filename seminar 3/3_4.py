# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

lst = [input ("Введите элемент: ") for i in range(int(input("Введите длину списка: ")))]
print(*lst)

res = [lst[i] > lst[i - 1] for i in range(1, len(lst))]
print(sum(res))