import numpy as np

counter = 0
m1 = []
m2 = []
def Mmatrix():
    global m1
    global counter
    global m2
    matrix = []
    print('Введите количество строк')
    x = int(input())
    print('Введите количество столбцов')
    y = int(input())
    for i in range(x):
        row = input().split()
        for j in range(y):
            row[j] = int(row[j])
        matrix.append(row)
    if counter == 0:
        m1 = matrix
        print(m1)
    else:
        m2 = matrix
        print(m2)
    counter += 1
Mmatrix()
Mmatrix()

matrix1 = np.array(m1)
matrix2 = np.array(m2)

print('Что вы хотите сделать с матрицами умножить(напишите *) или сложить(напишите +):')
if input() == '*':
    print(matrix1.dot(matrix2))
else:
    print(matrix1 + matrix2)
