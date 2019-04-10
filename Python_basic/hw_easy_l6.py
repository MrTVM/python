# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:
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


class SportCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print('{} {} поехала'.format(self.color, self.name))

    def stop(self):
        print('{} {} остановилась'.format(self.color, self.name))

    def turn(self, direction):
        print('{} {} повернула {}'.format(self.color, self.name, direction))


class WorkCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print('{} {} поехала'.format(self.color, self.name))

    def stop(self):
        print('{} {} остановилась'.format(self.color, self.name))

    def turn(self, direction):
        print('{} {} повернула {}'.format(self.color, self.name, direction))


class PoliceCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    def go(self):
        print('{} {} поехала'.format(self.color, self.name))

    def stop(self):
        print('{} {} остановилась'.format(self.color, self.name))

    def turn(self, direction):
        print('{} {} повернула {}'.format(self.color, self.name, direction))


if __name__ == '__main__':
    car1 = TownCar(100, 'black', 'toyota')
    print(car1.color, car1.name)
    print('Это полицеская машина? ', car1.is_police)
    car1.go()
    car1.turn('налево')
    car1.stop()
