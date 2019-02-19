import os
import psutil
import sys
import shutil

# print(os.listdir())
# for line in os.listdir():
#     line += '.fuck'
#     print(line)
#
# for line in os.listdir():
#     print(line)
#
# i = 0
# while i < len(os.listdir()):
#     os.listdir()[i] += 'ff'
#     i += 1
#
# for line in os.listdir():
#     print(line)

answer = 'y'

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
            print("Информация о системе: ")
            print (f"Count  of process: {psutil.cpu_count()}")
            print(f"Platform: {sys.platform}")
            print(f"Code of file system: {sys.getfilesystemencoding()}")
            print(f"Current directory: {os.getcwd()}")
            print(f"Current user: {os.getlogin()}")

        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print('Dublicate')
            list_of_files = os.listdir()
            i = 0
            while i < len(list_of_files):
                if os.path.isfile(list_of_files[i]):
                    new_files = list_of_files[i] + '.dupl'
                    shutil.copy(list_of_files[i], new_files)
                i += 1
        elif do == 5:
            print(os.listdir())
            list_of_files = os.listdir()
            number_of_file = int(input("Enter number of file wich need to dublicate: "))
            if os.path.isfile(list_of_files[number_of_file]):
                new_file = list_of_files[number_of_file] + ".txt"
                shutil.copy(list_of_files[number_of_file], new_file)
            else:
                print("It`s not file")
        elif do == 6:
            #list_of_files = os.listdir('C:/Users/Admin/PycharmProjects/untitled/Courses/ ')
            path = input("Enter path")
            list_of_files = os.listdir(path)
            flg = False
            if len(list_of_files) != 0:
                for i in range(len(list_of_files)):
                    if list_of_files[i].find(".dupl") != -1 and list_of_files[i].endswith(".dupl"):
                    # if list_of_files[i].find(".dupl") != -1 and (len(list_of_files[i]) - list_of_files[i].rfind('.dupl') == 5):
                        if os.path.isfile(list_of_files[i]):
                            print(f"Delete file: {list_of_files[i]}")
                            os.remove(list_of_files[i])
                            flg = True
            if not flg:
                print("In directory no files with '.dupl' ")
        else:
            pass

    elif answer == 'n':
        print('До свидания!')
        break
    else:
        print('Неизвестный ответ')