import turtle

turtle.setworldcoordinates(-2, -1.5, 1, 1.5)
t = turtle.Turtle()
turtle.tracer(0)

def fun(c):
    z = 0
    for _ in range(1000):
        z = z**2 + c
        if(abs(z) > 2):
            return False
    
    return True

for x in range(-200, 100):
    for y in range(-150, 150):
        c = complex(x/100, y/100)
        if(fun(c)):
            t.penup()
            t.goto(x/100, y/100)
            t.pendown()
            t.dot(3.5, 'black')

t.hideturtle()
turtle.update()
turtle.done()
        