import random
import cmath
import turtle

t = turtle.Turtle()
turtle.setworldcoordinates(0, 0, 10, 10)
t.pensize(1)
t.pencolor('black')

count = 0
for _ in range(5):
    x = random.random()
    y = random.random()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.dot(2, 'red')
    i = complex(x, y)
    tu = cmath.polar(i)
    if tu[0] < 1:
        count += 1
turtle.done()
print(count)
