import os
import psutil
import sys
import shutil

answer = 'y'


def dublicate_file(filename):
    if os.path.isfile(filename):
        new_file = filename + '.dupl'
        shutil.copy(filename, new_file)
        if os.path.exists(new_file):  # проверка существования файла
            print(f"Fiel {new_file} is created")
            return True
        else:
            print("File not created")
            return False


def sys_info():
    print("Information of system: ")
    print(f"Count  of process: {psutil.cpu_count()}")
    print(f"Platform: {sys.platform}")
    print(f"Code of file system: {sys.getfilesystemencoding()}")
    print(f"Current directory: {os.getcwd()}")
    print(f"Current user: {os.getlogin()}")


def removed(list_of_files):
    amount = 0
    if len(list_of_files) != 0:
        for i in range(len(list_of_files)):
            if list_of_files[i].endswith(".dupl"):
                if os.path.isfile(list_of_files[i]):
                    os.remove(list_of_files[i])
                    if not os.path.exists(list_of_files[i]):
                        amount += 1
                        print(f"Delete file: {list_of_files[i]}")
    else:
        return 0
    return amount


while True:
    answer = input('Давайте поработаем? (Y/N): ').lower()
    if answer == 'y':
        print(' [1] - выведу список файлов')
        print(' [2] - выведу информацию о системе')
        print(' [3] - выведу список процессов')
        print(' [4] - продублировать файлы в текущей директории')
        print(' [5] - дублровать указаннный файл')
        print(' [6] - удалить файлы с окнчанием .dupl')
        do = int(input('Укажите номер действия: '))
        if do == 1:
            print(os.listdir())
        elif do == 2:
            sys_info()

        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print('Dublicate')
            list_of_files = os.listdir()
            i = 0
            while i < len(list_of_files):
                dublicate_file(list_of_files[i])
                i += 1
        elif do == 5:
            print(os.listdir())
            list_of_files = os.listdir()
            number_of_file = int(input("Enter number of file which need to dublicate: "))
            if os.path.isfile(list_of_files[number_of_file]):
                dublicate_file(list_of_files[number_of_file])
            else:
                print("It`s not file")
        elif do == 6:
            # list_of_files = os.listdir('C:/Users/Admin/PycharmProjects/untitled/Courses/ ')
            path = input("Enter path")
            list_of_files = os.listdir(path)
            amount = removed(list_of_files)
            if amount != 0:
                print(f"Count of removed files - {amount}")
            else:
                print("Nothing removed")

        else:
            pass

    elif answer == 'n':
        print('До свидания!')
        break
    else:
        print('Неизвестный ответ')
