import turtle
import math

pi = 3.14159
t = turtle.Turtle()
turtle.setworldcoordinates(-2*pi, -2*pi, 2*pi, 2*pi)
turtle.tracer(0)

t.penup()
t.goto(-6, 0)
t.pendown()
t.goto(6, 0)
t.penup()
t.goto(0, -6)
t.pendown()
t.goto(0, 6)
t.goto(0, 0)

t.pensize(2)

flag = True
t.pencolor("#26f22f")
for xn in range(int(-2 * pi * 100), int(2 * pi * 100), 2):
    if flag:
        t.penup()
    x = xn / 100
    y = math.sin(x)
    t.goto(x, y)
    if flag:
        t.pendown()
        t.write("y=math.sin(x)", font=("consolas", 18, "normal"))
        flag = False

flag = True
t.pencolor("#eb1122")
for xn in range(int(-2 * pi * 100), int(2 * pi * 100), 2):
    if flag:
        t.penup()
    x = xn / 100
    y = math.cos(x)
    t.goto(x, y)
    if flag:
        t.pendown()
        t.write("y=math.cos(x)", font=("consolas", 18, "normal"))
        flag = False

flag = True
t.pencolor("#2613cd")
for xn in range(int(-2 * pi * 100), int(2 * pi * 100), 2):
    if flag:
        t.penup()
    x = xn / 100
    y = 2*math.cos(2*x)
    t.goto(x, y)
    if flag:
        t.pendown()
        t.write("y=math.2cos(2x)", font=("consolas", 18, "normal"))
        flag = False

t.hideturtle()
turtle.update()
turtle.done()