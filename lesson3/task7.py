# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


# user_list = [int(i) for i in input('ВВедите список чисел через пробел: ').split()]
user_list = [45, 12, -45, 12, 59, 5, 82, 63, 24, 754, 5, 5, 12, 5, 15, 12]

min_num = user_list.pop(user_list.index(min(user_list)))
min_num_2 = user_list.pop(user_list.index(min(user_list)))

print(min_num, min_num_2)
