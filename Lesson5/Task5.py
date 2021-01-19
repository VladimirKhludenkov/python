'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''

import os
from random import random

dir_path = os.path.dirname(os.path.realpath(__file__))
fn = dir_path + r'\digits.txt'

print('Введите количество чисел, которые требуется записать (1 ... 100)')
nd = int(input())
digits = []
for i in range(nd):
    n = random()
    digits.append(str(n) + ' ')

print(digits)

with  open(fn, "w") as out_f:
    out_f.writelines(digits)

print('Данные записаны в файл')

with open(fn, "r") as my_f:
    content = my_f.read()
    print(f'Данные прочитаны из файла {fn}')
    print(content)
    dgs = (float(numb) for numb in content.split())
    print('Сумма чисел:', sum(dgs))

