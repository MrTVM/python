# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print('{} {} поехала'.format(self.color, self.name))

    def stop(self):
        print('{} {} остановилась'.format(self.color, self.name))

    def turn(self, direction):
        print('{} {} повернула {}'.format(self.color, self.name, direction))


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


if __name__ == '__main__':
    police_car = PoliceCar(120, 'white', 'lada')
    print(police_car.is_police)
    my_car = TownCar(100, 'black', 'toyota')
    print(my_car.is_police)
