from numpy import *

vect = array([(1.0,2.0,3.0), (12,11,10)])

print(f"Размерность матрицы: {str(vect.ndim)}" )

print(f"Размеры строк: {vect.shape}")

print("Кол-во элементов: " + str(vect.size))

print("Тип данных:"  + str(vect.dtype))

print("Размер элемента в байтах:" + str(vect.itemsize))

print(str(vect.data))

a = arange(10).reshape(2,5)# reshape делает из последовательности массив(NumPy) двухмерный по 5 элементов

print("*"*25)
print(a)

print(f"Размерность матрицы: {str(a.ndim)}" )

print(f"Размеры строк: {a.shape}")

print("Кол-во элементов: " + str(a.size))

print("Тип данных:"  + str(a.dtype))

print("Размер элемента в байтах:" + str(a.itemsize))

print(str(a.data))

#Тип массива м/б явно указан в момент создания
arr = array([[1,2],[3,4]], dtype = complex)
print(arr)

#По умолчанию тип создаваемого массива — float64.
#Функция zeros() создает массив нулей, а функция ones() — массив единиц:
#не забывать что чилса надо указывать в скобках
print("*"*25)
arr0 = zeros((3,5))
print(arr0)
print("*"*25)
arr1 = ones((3,5))
print(arr1)

# Функция empty() создает массив без его заполнения.
# Исходное содержимое случайно и зависит от состояния памяти на момент создания массива (то есть от того мусора, что в ней хранится):
print("*"*25)
arrE = empty((3,5))
print(arrE)
print(arrE.ndim)

# Для создания последовательностей чисел, в NumPy имеется функция, аналогичная range(), только вместо списков она возвращает массивы:
print("*"*25)
arrOfArange1 = arange(0,21,4)
print(arrOfArange1)
print("*"*25)
arrOfArange2 = arange(0,21,4)
print(arrOfArange2)

# функцию linspace() которая вместо шага в качестве одного из аргументов принимает число, равное количеству нужных элементов
print("*"*25)
arrOfLinspace = linspace(0,2,15)
print(arrOfLinspace)

# Одномерные массивы выводятся как строки, двухмерные — как матрицы, а трехмерные — как списки матриц.
print("*"*25)
c = arange(24).reshape(2,3,4)
print(c)
print(c.ndim)
# Если массив слишком большой, чтобы его печатать, NumPy автоматически скрывает центральную часть массива и выводит только его уголки:
# Eсли вам действительно нужно увидеть все, что происходит в большом массиве,
# выведя его полностью, используйте функцию установки печати set_printoptions():
