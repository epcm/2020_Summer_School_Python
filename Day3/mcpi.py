import random
import turtle
import cmath

t = turtle.Turtle()
turtle.setworldcoordinates(0, 0, 1050, 1050)
turtle.tracer(0)

n = 10000

t.fillcolor("#c9c3db")
t.begin_fill()
t.fd(1000)
t.left(90)
t.circle(1000, 90, 100)
t.lt(90)
t.fd(1000)
t.end_fill()
count = 0
for _ in range(n):
    x = random.random() * 1000
    y = random.random() * 1000
    t.penup()
    t.goto(x, y)
    t.pendown()
    i = complex(x, y)
    tu = cmath.polar(i)
    if tu[0] < 1000:
        t.dot(2, 'red')
        count += 1
    else:
        t.dot(2, 'blue')
t.penup()
t.goto(500, 1000)
t.pendown()
t.write("n = %d(pi = %f)" % (n, count / n * 4))
t.hideturtle()
turtle.update()
print(count / n * 4)
turtle.done()
