import os


def print_files(path, lvl=0):
    file_list = os.scandir(path)
    for file in file_list:
        if file.is_dir():
            print(' ' * (lvl * 2) + '-' + file.name)
            print(" " * ((lvl * 2) + 1) + "V")
            print_files(path + f'/{file.name}', lvl + 1)
        else:
            print(' ' * (lvl * 2) + file.name)


def main():
    path_name = input('please type a path')
    print_files(path_name)


main()
