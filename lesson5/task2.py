from collections import defaultdict
from collections import deque


def my_decimal(str):
    decimal_num = 0
    num = deque(str)
    num.reverse()
    for i in range(len(num)):
        decimal_num += my_table[num[i]] * 16 ** i
    return decimal_num


def my_hexadecimal(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in my_table:
            if my_table[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


signs = '0123456789ABCDEF'
my_table = defaultdict(int)
counter = 0
for sign in signs:
    my_table[sign] += counter
    counter += 1

num1 = input('Введите первое число: ').upper()
num2 = input('Введите второе число: ').upper()

print(f'Сумма чисел равна: {my_hexadecimal(my_decimal(num1) + my_decimal(num2))}')
print(f'Произведение чисел равно: {my_hexadecimal(my_decimal(num1) * my_decimal(num2))}')
