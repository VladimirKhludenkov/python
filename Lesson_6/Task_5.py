'''
5.	Реализовать класс Stationery (канцелярская принадлежность).
●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:

    def __init__(self, t='Stationery'):
        self.title = t
        print(self.title, 'создан')

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, n):
        super().__init__(n)
        print('Ручка создана')

    def draw(self):
        print('Это написано', self.title)


class Pencil(Stationery):
    def __init__(self, n):
        super().__init__(n)
        print('Карандаш создан')

    def draw(self):
        print('Это написано', self.title)


class Handle(Stationery):
    def __init__(self, n):
        super().__init__(n)
        print('Маркер создан')

    def draw(self):
        print('Это написано', self.title)


print('\n')
stationery = Stationery()
stationery.draw()

print('')
pen = Pen('Pen')
pen.draw()

print('')
pencil = Pencil('Pencil')
pencil.draw()

print('')
handle = Handle('Handle')
handle.draw()
