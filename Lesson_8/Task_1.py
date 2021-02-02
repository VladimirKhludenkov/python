"""
1.	Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class MyDate:
    #months = {'January':31, 'February':29,  'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self):
        print('MyDate создан. Это сообщение не должно выводиться \n так как объект класса не создаётся')

    # format DD-MM-YYYY
    @classmethod
    def convert(cls, dateString):
        vs = dateString.split('-')
        return [int(vs[0]), int(vs[1]), int(vs[2])]

    # format DD-MM-YYYY
    @staticmethod
    def checkValid(dateString):
        print('Проверяем:', dateString)
        vs = dateString.split('-')
        if len(vs) != 3:
            return False, 'Неправильный формат данных'
        if not vs[0].isdigit() or not vs[1].isdigit() or not vs[2].isdigit():
            return False, 'Не числовые значения'

        d = int(vs[0])
        m = int(vs[1])
        y = int(vs[2])

        if (y > 2100) or (y < 0):
            return False, 'Год должен быть в пределах 0-2100'
        if (m < 1) or (m > 12):
            return False, 'Месяц должен быть в пределах 1-12'
        if (d > MyDate.months[m]) or (d < 1):
            return False, 'Не правильное число дня месяца'

        return True, 'Правильный формат даты'



#list of test dates
myDates = ['21-10-2001', '21-10-2001-23', '21-10-2001rr', '51-10-2001', '21-110-2001', '21-05-20701', '1-1-199']

for myDate in myDates:
    res, mess = MyDate.checkValid(myDate)
    if res == True:
        lst = MyDate.convert(myDate)
        print(f'Правильный формат даты. Числовые значения:\n{lst}')
    else:
        print(mess)
    print('')
