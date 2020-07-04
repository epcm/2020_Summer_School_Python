import turtle
import math
import random
import datetime

random.seed(datetime.datetime.now())
t = turtle.Turtle()

for _ in range(10):
    t.setheading(random.randint(0, 360))
    temp = math.cos(math.radians(t.heading() + 5)) / 8 + 0.25
    t.pencolor(temp*1.6, temp*1.2, temp*1.4)
    t.fd(100)
    print(temp)
turtle.done()
colors = ['#f44a55', 'white', '#ffcccc']