import turtle
import random
import math # вычисляет в радианах

M = 1

M = 2


def gotoxy(x, y):
    turtle.penup() # в указанную точку
    turtle.goto(x,y) #поднимаем перо
    turtle.pendown() # опускаем перо

def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill() # перед рисованием
    turtle.circle(r) # замкнутая фигура, которую закрашиваем
    turtle.end_fill()
    #turtle.speed(0) # придать ускорения движениию

gotoxy(0,0)
turtle.circle(80) # рисуем окружность
gotoxy(0,160)
draw_circle(5, "red")

phi = 360 / 7 # угол на который поделили окружность. В каждой части нах мал окр
r = 50 # радиус мал окр

for i in range (0,7): # функция range исп для формирования последовательности от 0 до 6
    phi_rad= phi* i * math.pi / 180.0 # перевод градусы угла в радианы
    gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r+ 60) # перемещение пера
    turtle.circle(22) # нарисовали барабан для патронов

gotoxy(math.sin(phi_rad)*r, math.cos(phi_rad)*r+ 60)
draw_circle(22, "brown")

answer = " "
while answer != "N":
    answer = turtle.textinput("Нарисовать окружность", "Y/N")
    if answer=="Y":
        turtle.penup()  # приготовили перо, между центрами окр, не будет соединительных линий
        turtle.goto(random.randrange(-300, 300), random.randrange(-200,
                                                                  200))  # будет не отрывать пера, значит между центрами будет соединительная линия
        turtle.pendown()  # убираем перо
        turtle.fillcolor(random.random(), random.random(), random.random())  # выбираем цвет
        turtle.begin_fill()  # перед рисованием

        turtle.circle(random.randrange(1, 100))  # замкнутая фигура, которую закрашиваем
        turtle.end_fill()  # конец рисования
    else:
        pass
