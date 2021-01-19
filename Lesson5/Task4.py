'''
Создать (не программно) текстовый файл со следующим содержимым: 
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

import os
import codecs


dir_path = os.path.dirname(os.path.realpath(__file__))
fn_in = dir_path + r'\in_numb_file.txt'
fn_out = dir_path + r'\out_numb_file.txt'
dict = {"1": "Один", "2": "Два", "3": "Три", "4": "Четыре", "5": "Пять", "6": "Шесть", "7": "Семь", "8": "Восемь", "9": "Девять", "0": "Нуль"}
en = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Null']
russ_phr = []

with codecs.open(fn_in, "r", encoding='utf-8') as my_f:   
    content = my_f.readlines()
#    print(content)

    for ln in content:
        # Обрезаем хвосты
        ln.rstrip()
        d = ln.split()
        if len(d) > 0 and d[0] in en:
            russ = f'{dict[d[2]]} - {d[2]}'
            russ_phr.append(russ)

    print(russ_phr)
    with codecs.open(fn_out, "w", encoding='utf-8') as my_f:
        for rp in russ_phr:
            my_f.write(rp + '\n')

