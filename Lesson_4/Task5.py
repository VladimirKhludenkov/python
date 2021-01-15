"""
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные числа от 100 до 1000 (включая границы).
Нужно получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


lst = [a for a in range(100, 1000 + 1) if a % 2 == 0]
print('Полученный список', lst)

print('Произведение. Вычисляем...')
print(reduce(my_func, lst))
