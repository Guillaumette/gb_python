# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

marks = list(map(int, input().split()))
print(marks)
max_l = max(marks)
min_l = min(marks)

result = [i if i != max_l else min_l for i in marks]
print(result)