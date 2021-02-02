"""
2.	Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivZeroError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.a > 0:
            return f'{self.a} / {self.b} = +Бесконечность'
        elif self.a < 0:
            return f'{self.a} / {self.b} = -Бесконечность'
        else:
            return f'{self.a} / {self.b} = Неопределённое значение'


# Dates for testing
values = [[15, 7], [12, 32], [6, 0], [-5, 0], [0, 8], [0, 0], ['a1', 'b2']]

for vls in values:
    val1, val2 = vls

    try:
        if val2 == 0:
            raise DivZeroError(val1, val2)
        c = val1 / val2
        print(f'{val1} / {val2} = {c}')

    except ValueError:
        print(f"Вы ввели не число: '{val1}' или '{val2}'")
    except DivZeroError as err:
        print(err)
    except TypeError:
        print(f'Вы ввели не число: "{val1}" или "{val2}"')
    except Exception as err:
        print(err)
