# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_lists(mas_1, mas_2):
    result_mas = []
    i = j = 0
    while i < len(mas_1) and j < len(mas_2):
        if mas_1[i] < mas_2[j]:
            result_mas.append(mas_1[i])
            i += 1
        else:
            result_mas.append(mas_2[j])
            j += 1
    if i < len(mas_1):
        result_mas += mas_1[i:]
    if j < len(mas_2):
        result_mas += mas_2[j:]

    return result_mas


def merge_sort(mas):
    if len(mas) == 1:
        return mas
    mid = len(mas) // 2
    left = merge_sort(mas[:mid])
    right = merge_sort(mas[mid:])
    return merge_lists(left, right)


my_mas = [random.randint(0, 50) for i in range(15)]

print(f'Исходный массив:\n{my_mas}')
print(f'Отсортированный массив:\n{merge_sort(my_mas)}')
