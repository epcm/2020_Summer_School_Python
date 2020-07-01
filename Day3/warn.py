import turtle


n = float(input("size:"))
turtle.speed(0)
turtle.delay(0)
turtle.hideturtle()
t = turtle.Turtle()

# 绘制主体
t.pencolor('black')
t.pensize(n*0.084)
t.fillcolor('yellow')

t.penup()
t.backward(n//2)
t.pendown()

t.begin_fill()
for _ in range(3):
    t.forward(n)
    t.circle(n*0.052, 120, int(n))
t.end_fill()

# 灵魂黄边
t.pencolor('yellow')
t.pensize(n/100)

t.penup()
t.right(90)
t.forward(n * 0.042)
t.left(90)
t.pendown()
for _ in range(3):
    t.forward(n)
    t.circle(n*0.0943, 120, int(n))
t.penup()
t.left(90)
t.forward(n * 0.042)
t.right(90)
t.pendown()

# 绘制叹号圆圈
t.pencolor('black')
t.pensize(1)
t.fillcolor('black')

t.penup()
t.forward(n / 2)
t.left(90)
t.forward(n * 0.094)
t.right(90)
t.pendown()
t.begin_fill()
t.circle(n * 0.0446,None, int(n))
t.end_fill()

# 绘制叹号上部
t.penup()
t.left(90)
t.forward(n * 0.14)
t.pendown()
t.right(10.3)
t.begin_fill()
t.forward(n * 0.329)
t.left(10.3)
t.circle(n * 0.0588, 180, int(n))
t.left(10.3)
t.forward(n * 0.329)
t.end_fill()


t.hideturtle()