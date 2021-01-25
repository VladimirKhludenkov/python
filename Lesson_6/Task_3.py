'''
3.	Реализовать базовый класс Worker (работник).
●	определить атрибуты: name, surname, position (должность), income (доход);
●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
●	создать класс Position (должность) на базе класса Worker;
●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
●	проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''

class Worker:
    def __init__(self, pos, n, sn):
        self.name = n
        self.surname = sn
        self.position = pos
        self.__income = {"wage": 0, "bonus": 0}
        print("Worker was created")

    @property
    def income(self):
        return self.__income

    def setWage(self, w):
        self.__income['wage'] = w

    def setBonus(self, b):
        self.__income['bonus'] = b

class Position(Worker):
    def get_full_name(self):
        return (self.name + ' ' + self.surname)

    def get_total_income(self):
        w = self.income['wage']
        b = self.income['bonus']
        return (w + b)

    def get_position(self):
        return self.position



print('')
manager = Position('Менеджер', 'Степан', 'Григорьев')
manager.setWage(100)
manager.setBonus(10)
print(f'Полное имя: {manager.get_full_name()}')
print(f'Должность: {manager.get_position()}')
print(f'Суммарный доход: {manager.get_total_income()}')

print('')
seller = Position('Продавец', 'Алла', 'Акиньшина')
seller.setWage(150)
seller.setBonus(25)
print(f'Полное имя: {seller.get_full_name()}')
print(f'Должность: {seller.get_position()}')
print(f'Суммарный доход: {seller.get_total_income()}')

print('')
director = Position('Директор', 'Иван', 'Ткоев')
director.setWage(1000)
director.setBonus(500)
print(f'Полное имя: {director.get_full_name()}')
print(f'Должность: {director.get_position()}')
print(f'Суммарный доход: {director.get_total_income()}')
