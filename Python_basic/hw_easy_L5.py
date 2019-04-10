# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os
import shutil


def create_dir(count_dir):
    for i in range(1, count_dir + 1):
        try:
            os.mkdir('dir_' + str(i))
            print('директория {} создана!'.format('dir_' + str(i)))
        except FileExistsError:
            print('директория {} уже существует!'.format('dir_' + str(i)))
            continue
    print('Нужные директории созданы!')


def del_dir(count_dir):
    for i in range(1, count_dir + 1):
        try:
            os.rmdir('dir_' + str(i))
            print('директория {} удалена!'.format('dir_' + str(i)))
        except FileNotFoundError:
            print('директория {} не существует!'.format('dir_' + str(i)))
            continue
    print('Нужные директории удалены!')


create_dir(9)
del_dir(9)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


print([name_dir for name_dir in os.listdir() if os.path.isdir(name_dir)])

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def current_file_copy():
    name_file = os.path.abspath(__file__)
    name_file = os.path.split(name_file)
    new_file = str(name_file[1].split('.')[0]) + '_copy.py'
    new_file = str(name_file[0]) + '/' + new_file
    if not os.path.isfile(new_file):
        shutil.copy(os.path.abspath(__file__), new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'


print(current_file_copy())

