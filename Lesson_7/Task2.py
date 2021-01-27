"""
2)	Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Dress(ABC):
    def __init__(self, typeCloth='Not defined'):
        self.typeCloth = typeCloth
        self.__cloth = 0

    # Здесь хотел добавить ещё @abstractmethod,
    # но питон сказал, что их нельзя совмещать
    @staticmethod
    def getNeedCloth(self, param):
        pass

    @property
    def cloth(self):
        return self.__cloth

    @cloth.setter
    def cloth(self, cloth):
        self.__cloth = cloth

    def __str__(self):
        st = f'{self.typeCloth}, need cloth {self.__cloth}'
        return st


class Coat(Dress):
    def __init__(self):
        Dress.__init__(self, 'Coat')

    @staticmethod
    def getNeedCloth(v):
        cloth = v / 6.5 + 0.5
        return cloth


class Suit(Dress):
    def __init__(self):
        Dress.__init__(self, 'Dress')

    @staticmethod
    def getNeedCloth(h):
        cloth = 2 * h + 0.3
        return cloth


class SewingStudio:
    def __init__(self, name='No name'):
        self.name = name
        print(f'Ателье "{self.name}" открыто!')
        self.totalCloth = 0

    def purchase(self, coats, suits):
        print(f'Заказ: Пальто (размер/количество): {coats}.  Костюмы (размер/количество): {suits}')

        for i in coats.keys():
            cl = Coat.getNeedCloth(int(i))
            self.totalCloth += cl * coats[i]
        for i in suits.keys():
            cl = Suit.getNeedCloth(int(i))
            self.totalCloth += cl * suits[i]

    def getTotalCloth(self):
        return self.totalCloth


# Создание ателье
ss = SewingStudio('Лучшее швейное ателье')

# Формируем заказ. Размер:количество
cts = {54: 3, 52: 5, 56: 1}
sts = {10: 2, 12: 4}

# Делаем заказ
ss.purchase(cts, sts)

# Смотрим сколько нужно ткани
clo = ss.getTotalCloth()

print(f'На заказ требуется {int(clo + 0.5)} ткани')
