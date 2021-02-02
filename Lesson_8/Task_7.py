"""
7.	Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class MyComplex:
    def __init__(self, a=0, b=0):
        self.re = a
        self.im = b

    def __add__(self, other):
        c = self.re + other.re
        d = self.im + other.im
        return MyComplex(c, d)

    def __sub__(self, other):
        c = self.re - other.re
        d = self.im - other.im
        return MyComplex(c, d)

    def __mul__(self, other):
        a1 = self.re
        b1 = self.im
        a2 = other.re
        b2 = other.im
        c = (a1 * a2 - b1 * b2)
        d = (a1 * b2 + b1 * a2)
        return MyComplex(c, d)

    def __truediv__(self, other):
        a1 = self.re
        b1 = self.im
        a2 = other.re
        b2 = other.im
        c = (a1 * a2 + b1 * b2) / (a2 * a2 + b2 * b2)
        d = (a2 * b1 - a1 * b2) / (a2 * a2 + b2 * b2)
        return MyComplex(c, d)

    def __str__(self) -> str:
        s = str(self.re)
        if self.im < 0:
            s += " - "
        else:
            s += " + "

        s += str(abs(self.im))
        s += "i"
        return (s)


compl1 = MyComplex(1, 2)
compl2 = MyComplex(5, -8)
print(f'Первая матрица c1 = {compl1}')
print(f'Вторая матрица c2 = {compl2}')

c = compl1 + compl2
print(f'c1 + c2 = {c}')

c = compl1 - compl2
print(f'c1 - c2 = {c}')

c = compl1 * compl2
print(f'c1 * c2 = {c}')

c = compl1 / compl2
print(f'c1 / c2 = {c}')
