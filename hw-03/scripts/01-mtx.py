'''
Нужно реализовать небольшую библиотеку для работы с матрицами
3.1
Сделать класс матрицы, в котором определить операции сложения и умножения (матричного и покомпонентного) через перегрузку операторов +, *, @ (как в numpy). Вызывать исключения, если матрицы на входе некорректной размерности (ValueError)
Сгенерировать две матрицы через np.random.randint(0, 10, (10, 10)) c seed-ом 0 и над ними провести все три операции. Записать результаты в текстовые файлы, названные matrix+.txt, matrix*.txt, matrix@.txt, соответственно. Это будет артефактом задачи.
'''

import numpy as np
import sys

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if self.matrix.shape != other.matrix.shape:
            raise ValueError('Matrix dimensions must agree')
        return Matrix(self.matrix + other.matrix)

    def __mul__(self, other):
        if self.matrix.shape != other.matrix.shape:
            raise ValueError('Matrix dimensions must agree')
        return Matrix(self.matrix * other.matrix)

    def __matmul__(self, other):
        if self.matrix.shape[1] != other.matrix.shape[0]:
            raise ValueError('Matrix dimensions must agree')
        return Matrix(self.matrix @ other.matrix)

    def __str__(self):
        return str(self.matrix)
    
    def __repr__(self):
        return str(self.matrix)
    
    def __eq__(self, other):
        return np.array_equal(self.matrix, other.matrix)
    
    def __ne__(self, other):
        return not np.array_equal(self.matrix, other.matrix)
    
    def __lt__(self, other):
        return np.all(self.matrix < other.matrix)
    
    def __le__(self, other):
        return np.all(self.matrix <= other.matrix)
    
    def __gt__(self, other):
        return np.all(self.matrix > other.matrix)
    
    def __ge__(self, other):
        return np.all(self.matrix >= other.matrix)
    
    def __getitem__(self, key):
        return self.matrix[key]
    
    def __setitem__(self, key, value):
        self.matrix[key] = value

def main():
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix3 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix4 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix5 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix6 = Matrix(np.random.randint(0, 10, (10, 10)))

    matrix12 = matrix1 + matrix2
    matrix56 = matrix5 @ matrix6
    matrix34 = matrix3 * matrix4

    artifacts_dir = '/Users/leonidkorotkevich/MEGA/work/itmo/py/hw-03/artifacts'
    np.savetxt(f'{artifacts_dir}/matrix+.txt', matrix12.matrix, fmt='%d')
    np.savetxt(f'{artifacts_dir}/matrix*.txt', matrix34.matrix, fmt='%d')
    np.savetxt(f'{artifacts_dir}/matrix@.txt', matrix56.matrix, fmt='%d')

if __name__ == '__main__':
    main()