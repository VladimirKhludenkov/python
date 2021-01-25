'''
1.	Создать класс TrafficLight (светофор).
●	определить у него один атрибут color (цвет) и метод running (запуск);
●	атрибут реализовать как приватный;
●	в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
●	продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
●	переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
●	проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

'''
import time

class TrafficLight:
    def __init__(self):
        print('Светофор')

    __color = 'red'
    pauses = {'red': 7, 'yellow': 2, 'green': 10}

    def running(self, start_color = 'red', green_state_len = 10):
        TrafficLight.__color = start_color
        TrafficLight.pauses['green'] = green_state_len
        print('TrafficLight is run...')

        while True:
            print('Светится:', TrafficLight.__color)
            time.sleep(TrafficLight.pauses[TrafficLight.__color])

            if(TrafficLight.__color == 'green'):
                TrafficLight.__color = 'yellow'

            elif(TrafficLight.__color == 'yellow'):
                TrafficLight.__color = 'red'

            elif(TrafficLight.__color == 'red'):
                TrafficLight.__color = 'green'


tl = TrafficLight()

# Init state, green tiime elapsing
tl.running('red', 4)

