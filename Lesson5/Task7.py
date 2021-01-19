'''
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки. 
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков). 
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''

import codecs
import os
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
fn_in = dir_path + r'\firms_in.txt'
fn_out = dir_path + r'\firms_out.txt'
dict_firms = {}
profit = []
json_obj = []

with codecs.open(fn_in, mode='r', encoding='utf-8') as f:
    for firm in f:
        #print (firm)
        f = firm.split()
        pr = float(f[2]) - float(f[3])
        profit.append(pr)
        dict_firms[f[0]] = pr

#print(dict_firms)
aver_prof = int(sum(profit) / len(profit))
#print(aver_prof)
json_obj.append(dict_firms)
json_obj.append({"average_profit": aver_prof})
print(json_obj)

# У меня почему-то в файл всё в одну строку записывается. Хотя я читал, что с красивыми отступами всё должно получиться...
with codecs.open(fn_out, "w", encoding='utf-8') as write_f:
    json.dump(json_obj, write_f)


    