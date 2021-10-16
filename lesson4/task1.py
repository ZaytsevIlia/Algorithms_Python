# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках практического задания первых трех уроков.

# для разбора взял 7-е задание 3-го урока.
import time
import random

user_list = []
for x in range(1000):
    user_list.append(random.randint(1, 5001))

# Способ 1

start_time = time.time()
num_min = min(user_list)
num_max = max(user_list)

print(sum(user_list[user_list.index(num_min) + 1:user_list.index(num_max)]))

print('Время исполнения', time.time() - start_time)

# Способ 2
start_time = time.time()

num_min_2 = user_list[0]

for i in range(1, len(user_list)):
    if user_list[i] < num_min_2:
        num_min_2 = user_list[i]

num_max_2 = user_list[0]

for i in range(1, len(user_list)):
    if user_list[i] > num_max_2:
        num_max_2 = user_list[i]

print(sum(user_list[user_list.index(num_min_2) + 1:user_list.index(num_max_2)]))

print('Время исполнения', time.time() - start_time)


# Временная разница получилась незначительная, ~ 0,0003 сек.
# Оба способа имеют линейную сложность O(n), в них идёт обычный перебор последовательности.
