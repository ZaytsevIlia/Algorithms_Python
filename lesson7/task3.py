# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках.

# Использовал сортировку слиянием

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


m = int(input('Массив имеет размер 2m + 1. Введите переменную "m": '))
my_mas = [random.randint(0, 100) for i in range(2 * m + 1)]

print(f'Отсортированный массив:\n{merge_sort(my_mas)}')
print(f'Медиана:\n{merge_sort(my_mas)[m]}')
