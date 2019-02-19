# matrix = [[0.5,0,0,0,0],
#           [1,0.5,0,0,0],
#           [1,1,0.5,0,0],
#           [1,1,1,0.5,0],
#           [1,1,1,1,0.5]] # это не матрица
# matrix_t = list(zip(*matrix))
#
# # # print(matrix)
# # # print(matrix_t)
# for line in matrix:
#      print(sum(line))
#      #print(line)
# #print(sum(line))
#
# print ("*"*25)
# for line in matrix_t:
#     print(list(line)) #преобразовние из кортежа в лист

#tuple - юолее экономичен чем список(list)
# tuple = (15,189.5,'hi',True)
# # tuple[2] = False #не подерживается присваивание
# print (tuple)
# print (tuple[1])
# # print (type(tuple))
# # print (dir(tuple))
#
# list  = [15,189.5,'hi',True]
# list[2] = False # поддерживается присваивание в списке

##########
a = [1,2,3,4,5]
b = [10,20,30,40,50]
c = [100,200,300,400,500]
d = [1000,2000,3000,4000,5000]
# zip с анг - застежка
result = list(zip(a,b,c))
# print(result) # выведет <zip object at 0x056B74B8> if result = zip(a,b,c)
print(result)

args  = [a,b,c,d]

result = list(zip(args))
print (result)
print("*"*25)
result = list(zip(*args))
print (result)
# звездочка для распоковки списка
# matrix_t = list(zip(*matrix)) - распоковывает matrix

# для установки  библотеки надо ввести в командной строке pip install "название библиотеки" (к примеру numpy)