# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и
# записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.


matrix = [
    [int(i) for i in input().split()],
    [int(i) for i in input().split()],
    [int(i) for i in input().split()],
    [int(i) for i in input().split()]
]

for i in matrix:
    print(*i, sum(i))
