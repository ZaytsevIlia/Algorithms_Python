# Определить количество различных подстрок с использованием хеш-функции.
# Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib


str = "billi"
N = len(str)
r = set()

for i in range(N):
    if i == 0:
        N = len(str) - 1
    else:
        N = len(str)
    for j in range(N, i, -1):
        print(str[i:j])
        r.add(hashlib.sha1(str[i:j].encode('utf-8')).hexdigest())
print(r)

print(f"Количество различных подстрок в строке '{str}' равно {len(r)}")
