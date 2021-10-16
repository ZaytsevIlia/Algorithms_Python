# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


# user_list = [int(i) for i in input('ВВедите список чисел через пробел: ').split()]
user_list = [45, 12, 45, 12, 59, 5, 82, -63, -24, -754, 0, -11, -12, -5, 12, 12]

negative_num = min(user_list)

for i in user_list:
    if (i >= negative_num) and (i < 0):
        negative_num = i

print(f'Макимальное отрицательное число: {negative_num}, индекс: {user_list.index(negative_num)}')
