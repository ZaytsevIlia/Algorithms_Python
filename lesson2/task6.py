import random

answer = random.randint(1, 100)
min = 1
max = 100
tryCount = 0
maxTryCount = 3
print(answer)
while tryCount != maxTryCount:
    user_answer = int(input(f'Угадайте число от {min} до {max} (У Вас {maxTryCount - tryCount} попыток): '))
    if user_answer == answer:
        print('Вы угадали!')
        break
    elif user_answer > answer:
        print('Число больше ответа.')
        max = user_answer
    elif user_answer < answer:
        print('Число меньше ответа')
        min = user_answer
    tryCount += 1
    if tryCount == 3:
        print(f'Ответ {answer}')
