user_num = int(input("Введите целое число: "))
answer = 0

while user_num > 0:
    number = user_num % 10
    user_num = user_num // 10
    answer = answer * 10
    answer = answer + number
print(f'"Обратное" число: {answer}')
