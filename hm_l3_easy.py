# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def pearson (name, age, city):
    print("{}, {} год(а), проживает в городе {}".format(name, age, city))


pearson('Василий', 21, 'Москва')


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def my_max(number_1, number_2, number_3):
    max_num = number_1
    if number_2 > number_1:
        max_num = number_2
    elif number_3 > number_1:
        max_num = number_3
    return max_num


print(my_max(4, 10, 7))


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def max_str(*args):
    max_ltr = 0
    for arg in args:
        if len(arg) > max_ltr:
            max_ltr = len(arg)
            max_list = arg
    return max_list


print(max_str('qwe', 'qwerty', 'asd'))

