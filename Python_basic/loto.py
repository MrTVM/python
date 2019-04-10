"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

"""


import random


class GameCard:
    def __init__(self, is_computer=False):
        self.is_computer = is_computer
        self.card = self._get_card()

    def _get_card(self):
        self.card = []
        count = 0
        for i in range(9):
            line = sorted(random.sample(list(range(1 + (i * 10), 10 + (i * 10))), k=3))
            # TO DO сделать проверку чтобы в строке было не более 5 чисел.
            if count < 15:
                counts = 2
            else:
                counts = 1
            choice_number = random.sample([0, 1, 2], k=random.randint(1, counts))
            for index in choice_number:
                line[index] = ''
                count = (3 - counts) + 1
            self.card.append(line)
        return self.card

    def print_card(self):
        if self.is_computer:
            print('---Карточка компьютера---')
        else:
            print('---Ваша карточка---')
        for i in range(3):
            print(' '.join(list(str(line[i]) for line in self.card)))

    def check_number(self, number):
        check_number_index = False

        for line in self.card:
            try:
                check_number_index = True
                new_line = line
                new_line[line.index(number)] = 'x'
                self.card[self.card.index(line)] = new_line
                break
            except ValueError:
                check_number_index = False
                continue
        return check_number_index


def del_number_in_bag(bags, keg_number):
    bags.remove(keg_number)
    return bags


def get_answer():
    while True:
        user_answer = input('Зачеркнуть цифру? (y/n) ')
        if user_answer == 'y' or user_answer == 'n':
            break
        else:
            print('Не понял что сделать? Зачеркнуть цифру? (y/n)')
    return user_answer


bag = list(range(1, 91))
player = GameCard()
computer = GameCard(True)

while len(bag) > 0:
    keg_in_bag = random.sample(bag, k=1)[0]
    print('Новый бочонок: {} (осталось {})'.format(keg_in_bag, len(bag) - 1))
    player.print_card()
    computer.print_card()
    answer = get_answer()
    if answer == 'y':
        result = player.check_number(keg_in_bag)
        if not result:
            print('Такого номера нет на карточке. Вы проиграли!')
            break
    else:
        result = player.check_number(keg_in_bag)
        if result:
            print('На вашей карточке был такой номер. Вы проиграли!')
            break
    computer.check_number(keg_in_bag)
    bag = del_number_in_bag(bag, keg_in_bag)
    if len(list(_.count('x') for _ in player.card)) == 15:
        print('Вы победили!')
    elif len(list(_.count('x') for _ in computer.card)) == 15:
        print('Победил компьютер!')
    else:
        print('Продолжаем!')
        continue

