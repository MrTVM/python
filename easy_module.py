import os


def create_dir(name_dir):
    if not name_dir:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(dir_path)
        print('директория {} создана!'.format(name_dir))
    except FileExistsError:
        print('директория {} уже существует!'.format(name_dir))


def del_dir(name_dir):
    if not name_dir:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена!'.format(name_dir))
    except FileNotFoundError:
        print('директория {} не существует!'.format(name_dir))


def view_current_dir(_):
    print(os.listdir())


if __name__ == '__main__':
    create_dir('test')
    del_dir('test')
    view_current_dir('')

