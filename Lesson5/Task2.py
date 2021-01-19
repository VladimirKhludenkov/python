'''
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
'''

import os
import codecs

# Путь к каталогу расположения питоновского файла
dir_path = os.path.dirname(os.path.realpath(__file__))
fn = dir_path + r'\inp_file.txt'


with codecs.open(fn, "r", encoding='utf-8') as in_file:
    content = in_file.readlines()
    #print(content)
    print(f'Файл {fn} прочитан. Содержимое файла:')
    print(content)
    print('Количество строк в файле:', len(content))
    print('')
    for s in content:
        s.rstrip()
        # Обрезаем хвосты
        w = s.split()
        print(f'Количество слов в строке: {len(w)}')
