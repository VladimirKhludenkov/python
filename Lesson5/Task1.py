'''
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
'''

import os
import codecs

# Путь к каталогу расположения питоновского файла
dir_path = os.path.dirname(os.path.realpath(__file__))
fn = dir_path + r'\out_file.txt'
lines = []
print('Введите данные. Окончание ввода - пустая строка')

while  True:
    ln = input()
    if ln == '':
        break
    else:
        lines.append(ln + '\n')

with codecs.open(fn, "w", encoding='utf-8') as out_f:
    out_f.writelines(lines)
    print(f'Данные записаны в файл{fn}')

