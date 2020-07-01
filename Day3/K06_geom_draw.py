import turtle
import random
import math

t = turtle.Turtle()
turtle.setworldcoordinates(-350, -350, 350, 350)
turtle.tracer(0)


pi = 3.14159
# 绘制函数
def function(size):
    t.pensize(size)

    flag = True
    t.pencolor("#004c7f")
    for xn in range(int(-2 * pi * 100), int(2 * pi * 100), 2):
        if flag:
            t.penup()
        x = xn
        y = math.sin(x/100)*100
        t.goto(x, y)
        if flag:
            t.pendown()
            flag = False

    flag = True
    t.pencolor("#5e8dc4")
    for xn in range(int(-2 * pi * 100), int(2 * pi * 100), 2):
        if flag:
            t.penup()
        x = xn
        y = math.cos(x/100)*100
        t.goto(x, y)
        if flag:
            t.pendown()
            flag = False

    flag = True
    t.pencolor("#b3c7d2")
    for xn in range(int(-2 * pi * 100), int(2 * pi * 100), 2):
        if flag:
            t.penup()
        x = xn
        y = 2*math.cos(2*x/100)*100
        t.goto(x, y)
        if flag:
            t.pendown()
            flag = False

# 绘制多边形
def polygon(n, size, color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(n):
        t.fd(size)
        t.rt(360/n)
    t.end_fill()

function(2)
for _ in range(50):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.penup()
    t.goto(x, y)
    colorlist = ['#004c7f', '#5e8dc4', '#b3c7d2', '#84898c', '#a88d80', '#fbb898', '#fbb898']
    polygon(random.randint(3, 10), random.randint(25,40), random.choice(colorlist))

turtle.hideturtle()
turtle.update()
turtle.done()