import os
import sys
import psutil

# some_variable = [1,2,3]
# print(dir(some_variable))#что в ней есть (в типе)
# print(type(some_variable))#тип переменной
# print(help(some_variable))# описание типа
# print(dir(psutil))
# print(help(psutil.pids))

# print(psutil.pids())

answer = input('Давайте поработаем? (Y/N): ').lower()

if answer == 'y':
    print('Отлично, хозяин')
    print('Я умею:')
    print(' [1] - выведу список файлов')
    print(' [2] - выведу информацию о системе')
    print(' [3] - выведу список процессов')
    do = int(input('Укажите номер действия: '))
    if do == 1:
        print(os.listdir())
    elif do == 2:
        while True:
            print(' [4] - Имя текущей директории')
            print(' [5] - Название платформы')
            print(' [6] - Кодировка файловой системы')
            print(' [7] - Логин пользователя')
            print(' [8] - Количество CPU')
            do2 = int(input('Укажите номер действия: '))
            if do2 == 4:
                print(os.getcwd())
            elif do2 == 5:
                print(os.name)
            elif do2 == 6:
                print(sys.getfilesystemencoding())
            elif do2 == 7:
                print(os.getlogin())
            elif do2 == 8:
                print(psutil.cpu_count())
            choose = input("More?").lower()
            if choose == "n":
                break

    elif do == 3:
        print(psutil.pids())
    else:
        pass

elif answer == 'n':
    print('До свидания!')
else:
    print('Неизвестный ответ')