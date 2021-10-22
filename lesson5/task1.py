import collections

num_comp = int(input('Введите количество предприятий: '))

my_dict = collections.defaultdict()
# my_dict = {'Test1': [50, 100, 100, 100], 'Test2': [100, 150, 20, 150], 'Test3': [200, 150, 100, 125],
#            'Test4': [200, 150, 100, 150]}

for i in range(num_comp):
    my_dict.setdefault(input('Введите наименование  предприятия: '),
                       [int(j) for j in input('Введите суммы прибыли по 4-ём кварталам: ').split()])


profit = 0
for val in my_dict.values():
    for i in val:
        profit += i

mid_profit = profit/num_comp

list_comp_big = []
list_comp_small = []

for key, val in my_dict.items():
    profit_comp = 0
    for i in val:
        profit_comp += i
    if profit_comp > mid_profit:
        list_comp_big.append(key)
    else:
        list_comp_small.append(key)

print('Компании у которых прибыль больше средней прибыли: ')
print(*list_comp_big, sep='\n')
print('Компании у которых прибыль меньше средней прибыли: ')
print(*list_comp_small, sep='\n')
