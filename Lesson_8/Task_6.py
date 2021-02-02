"""
5.	Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
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

    @property
    def state(self):
        if not self.__state in self.__states:
            self.__state = 'no defined'
        return self.__state

    @state.setter
    def state(self, value):
        if value in self.__states:
            self.__state = value
        else:
            # Euther no actions Or set to not defined state
            self.__state = 'no defined'

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

    # Ремонт оборудования
    def doRepair(self):
        self.state = 'ready'
        self.usingCycles = 0
        print(f'{self.name}: Ремонтируется')

    # Списание оборудования
    def toDispose(self):
        print(f'{self.name}: Отдано на списание: ')

    def __str__(self):
        c = f'Device: {self.name} \n price: {self.price} \n weight: {self.weight} \n size: {self.size} \n state: {self.state} \n using cycles: {self.usingCycles} \n maxUsingCycles: {self.maxUsingCycles}'
        return c


# Принтер
class Printer(Equipment):
    def __init__(self, pr=100, we=50, sz=30, st='ready', uc=0, myc=70):
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
    def __init__(self, pr=150, we=20, sz=30, st='ready', uc=0, myc=110):
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
    def __init__(self, pr=250, we=55, sz=20, st='ready', uc=0, myc=250):
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

    # Добавление техники на склад
    def Add(self, item, amount):
        needCapacity = item.size * amount
        if needCapacity > self.capacityFree:
            print('На складе не достаточно свободного места!')
            return False

        self.capacityFree -= needCapacity
        if item in self.equip.keys():
            amount += self.equip[item]
            self.equip[item] = amount
        else:
            self.equip[item] = amount

        print(f'Оборудование принято на склад, осталось свободного места {self.capacityFree}')
        return True

    # Запрос выдачи техники со склада
    def Remove(self, item, amount):
        if not item in self.equip.keys():
            print('Такого оборудования на складе нет')
            return False
        else:
            am = self.equip[item]
            if amount > am:
                print(f'Такого оборудования на складе меньше, чем запрашивается ({self.equip[item]})')
                return False, None

            self.equip[item] = am - amount
            availCapacity = item.size * amount

            self.capacityFree += availCapacity
            print(f'Оборудование выдано со склада, осталось свободного места {self.capacityFree}')

    # Показать список имущества
    def showInners(self):
        print('List of inners in Warehouse:')
        for i in self.equip:
            print(i)
            print(f' Amount: {self.equip[i]}\n')

    def __str__(self) -> str:
        c = f"Warehouse: {self.name} \n Total capacity: {self.capacityTotal} \n Free capacity: {self.capacityFree}"
        return c


helpStr = '''Для добавления оборудования на склад введите название создаваемого оборудования, его количество (штук),
и операцию добавления Add, например: "Scaner 5 Add"
Для изъятия оборудования со склада введите название оборудования, его количество (штук), и операцию удаления Rem:
например: "Printer 8 Rem"

Для отображения содержимого склада наберите "show"
Для помощи наберите "help"
Для завершения операций наберите "stop"'''


wh = Warehouse(1000, 'Самый лучший склад')
print(wh)
wh.showInners()
print(helpStr)

while True:
    print('Введите команду:')
    s = input().split()
    if s == ['stop']:
        print('quit...')
        break
    elif s == ['help']:
        print(helpStr)
    elif s == ['show']:
        wh.showInners()
    elif s == []:
        continue
    else:
        if not s[0] in ['Printer', 'Scaner', 'Copier']:
            print(helpStr)
        elif not s[1].isdigit():
            print(helpStr)
        elif not s[2] in ['Add', 'Rem']:
            print(helpStr)
        else:
            eq = None
            if s[0] == 'Scaner':
                eq = Scaner()
            elif s[0] == 'Printer':
                eq = Printer()
            elif s[0] == 'Copier':
                eq = Copier()

            amount = int(s[1])

            if s[2] == 'Add':
                wh.Add(eq, amount)
            elif s[2] == 'Rem':
                wh.Remove(eq, amount)

            wh.showInners()
