import string

leters = string.ascii_lowercase

num_leter = int(input('Введите номер буквы: '))
leter = leters[num_leter - 1]
print(leter)
