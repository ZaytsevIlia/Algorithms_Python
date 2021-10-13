# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


# user_list = [int(i) for i in input('ВВедите список чисел через пробел: ').split()]
user_list = [45, 12, -45, 12, 59, 5, 82, 63, 24, 754, 5, 5, 12, 5, 12, 12]

num_min = min(user_list)
num_max = max(user_list)

print(sum(user_list[user_list.index(num_min) + 1:user_list.index(num_max)]))
