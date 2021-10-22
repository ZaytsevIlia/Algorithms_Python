# Написать два алгоритма нахождения i-го по счёту простого числа.

# Без использования Решета Эратосфена;

import time


n = int(input())
start_time = time.time()
numb_s = [i for i in range(n * n)]
numb_s[0] = numb_s[1] = 0

prime_numb_s = []
for i in range(2, len(numb_s)):
    for num in prime_numb_s:
        if numb_s[i] % num == 0:
            break
    else:
        prime_numb_s.append(numb_s[i])

    if len(prime_numb_s) == n:
        print(prime_numb_s[-1])
        break
print('Время исполнения', time.time() - start_time)


# Использовать алгоритм Решето Эратосфена

n = int(input())
start_time = time.time()
numb = [i for i in range(n * n)]
numb[0] = numb[1] = 0

i = 2
prime_numb = []
while len(prime_numb) < n:
    if numb[i] != 0:
        prime_numb.append(numb[i])
        j = i * 2
        while j < len(numb):
            numb[j] = 0
            j += i
    i += 1

print(prime_numb[-1])
print('Время исполнения', time.time() - start_time)


# Время исполнения кода по алгоритму решето Эратосфена, быстре чем способ с обычным перебором чисел последовательности.
# При вычислении 100-го простого числа скорость Решета Эратосфена быстрее на ~0,006 сек.

# Сложность способа без использования Решета Эратосфена = O(n2)
# Сложность способа с использованием Решета Эратосфена = O(n2)

# Данную оценку алгоритма я дал, потому что они состоят из двух вложенных циклов.
