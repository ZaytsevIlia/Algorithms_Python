# Определить, какое число в массиве встречается чаще всего.


user_list = [int(i) for i in input('ВВедите список чисел через пробел: ').split()]
# user_list = [45, 12, 45, 12, 59, 5, 82, 63, 24, 754, 5, 5, 12, 5, 12, 12]
user_set = set(user_list)

max_count = 0
num_max_count = 0

for i in user_set:
    if user_list.count(i) > max_count:
        max_count = user_list.count(i)
        num_max_count = user_list[i]

print(f'Цифра "{num_max_count}" встречается больше всего раз: {max_count}')
