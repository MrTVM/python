# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Pearson:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 50
        self.armor = 1.2

    def _calculate_damage(self, who_defend):
        return self.damage // who_defend.armor

    def attack(self, who_defend):
        damage = int(self._calculate_damage(who_defend))
        who_defend.health -= damage
        print('{} нанес {} ед. урона {}у и того осталось {} ед. здоровья'
              .format(self.name, damage, who_defend.name, who_defend.health))


class Player(Pearson):
    def __init__(self, name):
        super().__init__(name)
        self.armor = 1.2


class Enemy(Pearson):
    def __init__(self, name):
        super().__init__(name)
        self.armor = 0.7


class GameStart:
    def __init__(self):
        self.player = Player('Игрок')
        self.enemy = Enemy('Враг')

    def start(self):
        print('Игра началась!')
        last_attacker = self.enemy.name
        while self.player.health > 0 and self.enemy.health > 0:
            if last_attacker == self.player.name:
                self.enemy.attack(self.player)
                last_attacker = self.enemy.name
            else:
                self.player.attack(self.enemy)
                last_attacker = self.player.name
        if self.player.health > 0:
            print('{} победил!'.format(self.player.name))
        else:
            print('{} победил!'.format(self.enemy.name))
        print('Игра окончена!')


GameStart().start()

