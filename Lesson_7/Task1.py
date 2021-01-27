"""
1)	Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31	22
37	43
51	86

3	5	32
2	4	6
-1	64	-8

3	5	8	3
8	3	7	1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, m):
        self.elems = []
        for row in range(len(m)):
            a = m[row]
            r = []
            for col in range(len(a)):
                r.append(a[col])
            self.elems.append(r)

    def __str__(self):
        c = ''
        if self.elems is None:
            c += "Empty"
        else:
            for row in self.elems:
                for col in row:
                    c += str(col) + '\t'
                c += '\n'
        return c

    def fill(self, m):
        self.elems = []
        for row in range(len(m)):
            a = m[row]
            r = []
            for col in range(len(a)):
                r.append(a[col])
            self.elems.append(r)

    def __add__(self, other):
        els = []
        for row in range(len(self.elems)):
            a = self.elems[row]
            r = []
            for col in range(len(a)):
                r.append(self.elems[row][col] + other.elems[row][col])
            els.append(r)
        return Matrix(els)


mtx1 = Matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print('Первая матрица равна:')
print(mtx1)

mtx2 = Matrix([[21, 22, 23], [24, 25, 26], [27, 28, 29]])
print('Вторая матрица равна:')
print(mtx2)

mtx3 = mtx1 + mtx2
print('Сумма двух матриц равняется:')
print(mtx3)
