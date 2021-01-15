"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

print("Введите числа, через пробел")
lst = input().split()
# lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


out_lst = [lst[i] for i in range(1, len(lst)) if int(lst[i]) > int(lst[i - 1])]
print(f'Выходной список: {out_lst}')
