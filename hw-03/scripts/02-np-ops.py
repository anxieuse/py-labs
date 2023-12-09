'''
3.2
Используя примеси numpy, сделать класс, который будет уметь выполнять все стандартные арифметические операции.
Также добавить через примеси: запись объекта в файл, красивое отображение в консоли (__str__), getter-ы и setter-ы для полей класса
В самих классах должно быть минимальное количество методов
Артефакты задачи - аналогично задаче easy
'''

import numpy as np

class FileOperationsMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

class ConsoleDisplayMixin:
    def __str__(self):
        return f"ArithmeticOperations: {self.data}"

class AccessorsMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

class ArithmeticOperations(FileOperationsMixin, ConsoleDisplayMixin, AccessorsMixin):
    def __init__(self, data):
        self._data = np.array(data)

    def __add__(self, other):
        return ArithmeticOperations(self.data + other.data)

    def __sub__(self, other):
        return ArithmeticOperations(self.data - other.data)

    def __mul__(self, other):
        return ArithmeticOperations(self.data * other.data)

    def __truediv__(self, other):
        return ArithmeticOperations(self.data / other.data)

    def __pow__(self, other):
        return ArithmeticOperations(self.data ** other.data)

    def __mod__(self, other):
        return ArithmeticOperations(self.data % other.data)

    def __str__(self):
        return f"ArithmeticOperations: {self.data}"

# Пример использования
op1 = ArithmeticOperations([1, 2, 3])
op2 = ArithmeticOperations([4, 5, 6])

result = op1 + op2
print(result)
print(result.data)
print(result.data[0])
print(result.data[1])

result.save_to_file('../artifacts/result+.txt')

result = op1 - op2
print(result)
print(result.data)
print(result.data[0])
print(result.data[1])

result.save_to_file('../artifacts/result-.txt')

result = op1 * op2
print(result)
print(result.data)
print(result.data[0])
print(result.data[1])

result.save_to_file('../artifacts/result*.txt')

result = op1 / op2
print(result)
print(result.data)
print(result.data[0])
print(result.data[1])

result.save_to_file('../artifacts/resultdiv.txt')

result = op1 ** op2
print(result)
print(result.data)
print(result.data[0])
print(result.data[1])

result.save_to_file('../artifacts/resultpow.txt')

result = op1 % op2
print(result)
print(result.data)
print(result.data[0])
print(result.data[1])

result.save_to_file('../artifacts/resultmod.txt')
