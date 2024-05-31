import os


def del_files(files: list) -> None:
    for name in files:
        if os.path.isfile(name):
            os.remove(name)
            print(f'Файл {name} удален')

        else:
            print(f'Файл {name} не существует')


