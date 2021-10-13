# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


user_list = [int(i) for i in input('ВВедите список чисел через пробел: ').split()]

index_min = user_list.index(min(user_list))
index_max = user_list.index(max(user_list))

user_list[index_min], user_list[index_max] = user_list[index_max], user_list[index_min]

print(*user_list, sep=', ')
