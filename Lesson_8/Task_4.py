"""
4.	Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""


# Оборудование
class Equipment:
    # Name, Price, Weight, Size, State, Using cycles, Max using cycles
    def __init__(self, nm, pr, we, sz, st, uc, myc):
        self.__states = ['in use', 'ready', 'need repair', 'in service', 'no defined']
        # Текущее состояние
        self.__state = 'ready'
        self.name = nm
        self.price = pr
        self.weight = we
        self.size = sz
        self.state = st
        self.usingCycles = uc
        self.maxUsingCycles = myc
        # print(f'Equipment {self.name} create')

    # Некоторая абстрактная работа
    def doJob(self, cycles):
        self.usingCycles += cycles
        if self.usingCycles > self.maxUsingCycles:
            self.state = 'need repair'
            self.usingCycles = self.maxUsingCycles
            print(f'Equipment {self.name} need repair')
            return False
        else:
            print(f"Equipment {self.name} do job")
            return True


# Принтер
class Printer(Equipment):
    def __init__(self, pr=100, we=0, sz=0, st='ready', uc=0, myc=0):
        super().__init__('Printer', pr, we, sz, st, uc, myc)

    # Вывод на печать
    def doPrint(self, pages):
        if super.doJob(pages):
            print(f'Print {pages} pages')
        else:
            print('Printer need repair')
            return False


# Сканер
class Scaner(Equipment):
    def __init__(self, pr=0, we=0, sz=0, st='ready', uc=0, myc=0):
        super().__init__('Scaner', pr, we, sz, st, uc, myc)

        # Сканирование
        def doScan(self, pages):
            if super.doJob(pages):
                print(f'print {pages} pages')
            else:
                print('Scaner need repair')
                return False


# Копир (ксерокс)
class Copier(Equipment):
    def __init__(self, pr=0, we=0, sz=0, st='ready', uc=0, myc=0):
        super().__init__('Copier', pr, we, sz, st, uc, myc)

    # Копирование
    def toCopy(self, pages):
        if super.doJob(pages):
            print(f'print {pages} pages')
        else:
            print('Printer need repair')
            return False


# Склад
class Warehouse:
    def __init__(self, cap, nm='Simple Warehouse'):
        self.equip = {}
        self.name = nm
        self.capacityTotal = cap
        self.capacityFree = cap

    # Показать список имущества
    def showInners(self):
        print('List of inners:')
        if len(self.equip) == 0:
            print(' Empty Warehouse')
        for i in self.equip:
            print(i)
            print(f' Amount: {self.equip[i]}\n')

    def __str__(self) -> str:
        c = f"Warehouse: {self.name} \n Total capacity: {self.capacityTotal} \n Free capacity: {self.capacityFree}"
        return c


wh = Warehouse(1000, 'Самый лучший склад')
print(wh)
wh.showInners()
