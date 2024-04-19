# incomplete: entries[1] does not work entries is not iterable
import os


# entries = os.scandir('/home/pc/myCode')
#    entry_list = []
#    for entry in entries:
#        if (entry.is_dir()):
#            entry_list.append(entry.name)
#            print(entry)
#    print('=========================================')
#    for i in range(0, len(entry_list)):
#        deeper = os.scandir(f'/home/pc/myCode/{entry_list[i]}')
#        print(entry_list[i])
#        for x in deeper:
#            print(x)
#        print('=====================================')
#
# file:
#   file2,
#   file3:
#       file5
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
