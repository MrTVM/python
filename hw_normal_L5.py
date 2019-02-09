# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import easy_module as easy
import os
import sys


def print_help(_):
    print("help - получение справки")
    print("go_to_dir <dir_name> - перейти в папку")
    print("view - просмотреть содержимое текущей папки")
    print("delete_dir <dir_name> - удалить папку")
    print("create_dir <dir_name> - создать папку")


def change_dir(name_dir):
    if not name_dir:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.chdir(dir_path)
        print('Директория изменена. Текущая папка: {}'.format(os.getcwd()))
    except FileNotFoundError:
        print('директория {} не существует!'.format(name_dir))


do_it = {
    'help': print_help,
    'go_to_dir': change_dir,
    'view': easy.view_current_dir,
    'delete_dir': easy.del_dir,
    'create_dir': easy.create_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do_it.get(key):
        do_it[key](dir_name)
    else:
        print('Задан неверный ключ')
        print('Укажите ключ help для получения справки')


