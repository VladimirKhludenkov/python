'''
4.	Реализуйте базовый класс Car.
●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
'''

class Car:
    def __init__(self, n, c, isp):
        super().__init__()
        self.name = n
        self.color = c
        self.is_police = isp
        self.speed = 0
        print('Car is created')
        print(f'Name - {self.name}, Color - {self.color}')
   
    def go(self):
        print(self.name, 'поехал')
        
    def stop(self):
        print(self.name, 'остановился')
    
    def turn(self, direction):
        print(self.name, 'повернул', direction)

    def setSpeed(self, sp):
        self.speed = sp

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, n, c):
        super().__init__(n, c, False)
        print('Town car is created')
    def show_speed(self):
        super().show_speed()
        if (self.speed > 60):
            print(f'Внимание! Скорость превышена на {self.speed - 60} км/ч')

class SportCar(Car):
    def __init__(self, n, c):
        super().__init__(n, c, False)
        print('Sport car is created')
    def show_speed(self):
        super().show_speed()
        if (self.speed > 90):
            print(f'Хорошо едем!')

class WorkCar(Car):
    def __init__(self, n, c):
        super().__init__(n, c, False)
        print('Sport car is created')
    def show_speed(self):
        super().show_speed()
        if (self.speed > 40):
            print(f'Внимание! Скорость превышена на {self.speed - 40} км/ч')

class PoliceCar(Car):
    def __init__(self, n, c):
        super().__init__(n, c, True)
        print('Police car is created')
    def show_speed(self):
        super().show_speed()
        if (self.speed > 95):
            print(f'Всё равно догоним!')



tc = TownCar('TownCar', 'Blue')
sc = SportCar('SportCar', 'Red')
wc = WorkCar('WorkCar', 'Green')
pc = PoliceCar('PoliceCar', 'Yellow')

print()
tc.go()
tc.setSpeed(10)
tc.turn('Left')
tc.turn('Right')
tc.show_speed()
tc.setSpeed(100)
tc.show_speed()
tc.stop()

print()
wc.go()
wc.setSpeed(10)
wc.turn('Left')
wc.turn('Right')
wc.show_speed()
wc.setSpeed(100)
wc.show_speed()
wc.stop()

print()
sc.go()
sc.setSpeed(10)
sc.turn('Left')
sc.turn('Right')
sc.show_speed()
sc.setSpeed(100)
sc.show_speed()
sc.stop()

print()
pc.go()
pc.setSpeed(10)
pc.turn('Left')
pc.turn('Right')
pc.show_speed()
pc.setSpeed(105)
pc.show_speed()
pc.stop()

