user_num = int(input("Введите целое число: "))
even = set()
odd = set()

while user_num > 0:
    number = user_num % 10
    user_num = user_num // 10
    if number % 2 == 0:
        even.add(number)
    else:
        odd.add(number)

print(f'Чётные числа {even} \nНечётные числа {odd}')