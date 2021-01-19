'''
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''

import os
import codecs

sal_aver = []

# Путь к каталогу расположения питоновского файла
dir_path = os.path.dirname(os.path.realpath(__file__))
fn = dir_path + r'\stuff.txt'
print(f'Открываем файл {fn}')
with codecs.open(fn, encoding='utf-8') as my_f:
    content = my_f.readlines()
    print(content)

    print('Фамилии сотрудников с окладом менее 20 тысяч:')
    for s in content:
        # Обрезаем хвосты
        s.rstrip()
        sotr = s.split()
        salary = float(sotr[1])
        sal_aver.append(salary)
        if salary < 20000:
            print(f'{sotr[0]} : {salary}')
    print('Средний доход сотрудников:', sum(sal_aver) / len(sal_aver))


