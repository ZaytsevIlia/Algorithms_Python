symb = '+'

while symb != '0':
    a = int(input('Введите первое число: '))
    symb = input('Введите знак дейстия "+", "-", "*", "/" (если хотите выйти из программы введите "0"): ')
    b = int(input('Введите второе число: '))

    if symb == '+':
        print(a + b)
    elif symb == '-':
        print(a - b)
    elif symb == '*':
        print(a * b)
    elif symb == '/':
        if b == 0:
            print('Делить на ноль нельзя')
        else:
            print(a / b)
    elif symb != '0':
        print('Вы ввели неверный знак, попробуйте ещё раз: ')
