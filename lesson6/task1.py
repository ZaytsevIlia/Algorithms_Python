# После анализа трёх задач, можно сделать вывод, что первая задача затрачивает меньше памяти на переменные,
# даже в худшем своём случае, она затратит 112 байт, две остальные задачи затрачивают по 240 байт,
# это связано с использованием массива.
# Версия Python 3.9.5, разрядность ОС 64х
import sys

# Разбор задачи №1 урок №1

num = int(input('Введите трёхзначное число: '))  # Введённое трёхзначное число весит 28 байт

a = num//100            # 28 байт
b = num % 100//10       # 28 байт
c = num % 100 % 10      # 28 байт

print(a+b+c)
print(a*b*c)

print(f'На все переменные задачи потрачено '
      f'{sys.getsizeof(num) + sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c)} байт')  # 104, 108 или 112 байт
                                            # в зависимости от того, сколько нулей будет в ведённом трёхзначном числе


# Разбор задачи №4 урок №3
print('-'*50)

user_list = [45, 12, 45, 12, 59, 5, 82, 63, 24, 754, 5, 5, 12, 5, 12, 12]  # 184 байт =
                                                                  # 56 байт(пустой массив) + 8(число в массиве)*16 байт
user_set = set(user_list)


max_count = 0      # 24 байта, после цикла будет равен 28 байт, т.к. будет присвоено значение
num_max_count = 0  # 24 байта, после цикла будет равен 28 байт, т.к. будет присвоено значение
print(f'{sys.getsizeof(max_count)} байт')
print(f'{sys.getsizeof(num_max_count)} байт')


for i in user_set:
    if user_list.count(i) > max_count:
        max_count = user_list.count(i)
        num_max_count = user_list[i]


print(f'{sys.getsizeof(max_count)} байт')
print(f'{sys.getsizeof(num_max_count)} байт')

print(f'Цифра "{num_max_count}" встречается больше всего раз: {max_count}')

print(f'На все переменные задачи потрачено '
      f'{sys.getsizeof(user_list) + sys.getsizeof(max_count) + sys.getsizeof(num_max_count)} байт')  # Всего 240 байт


# Разбор задачи №7 урок №3
print('-'*50)

user_list = [45, 12, -45, 12, 59, 5, 82, 63, 24, 754, 5, 5, 12, 5, 15, 12]  # 184 байт =
                                                                  # 56 байт(пустой массив) + 8(число в массиве)*16 байт
print(f'{sys.getsizeof(user_list)} байт')

min_num = user_list.pop(user_list.index(min(user_list)))    # 28 байт
min_num_2 = user_list.pop(user_list.index(min(user_list)))  # 28 байт

print(f'{sys.getsizeof(min_num)} байт')
print(f'{sys.getsizeof(min_num_2)} байт')

print(min_num, min_num_2)

print(f'На все переменные задачи потрачено '
      f'{sys.getsizeof(user_list) + sys.getsizeof(min_num) + sys.getsizeof(min_num_2)} байт')  # Всего 240 байт
