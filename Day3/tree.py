import turtle
import random
import datetime
random.seed(datetime.datetime.now())

# 画正方形
def square(size, color, t):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()

# 画叶子
def leaf(size, color, t):
    t.rt(90)
    t.backward(size/2)
    #square(size, '#f44a55') #中
    t.rt(90)
    square(size, color, t) #左
    t.rt(180)
    square(size, color, t) #下
    t.fd(size)
    t.rt(90)
    square(size, color, t)
    t.fd(size)
    t.rt(90)
    square(size, color, t)
    t.fd(size)
    t.rt(90)
    t.fd(size/2)
    t.rt(90)


# 画树
def tree(branch_len, t):
    ang = random.randint(30,40)
    if branch_len > random.choice((10, 15)):
        t.pensize(branch_len/3)
        per = random.randint(75,83)/100#枝长缩短因子
        t.fd(branch_len)
        t.rt(ang)
        tree(branch_len*per, t)
        for _ in range(2):
            t.lt(ang)
            tree(branch_len*per, t)
        t.rt(ang)
        t.backward(branch_len)

    else:
        tow = t.heading()
        t1.seth(0)
        leaf(1.5, '#f44a55', t)
        t.seth(tow)

#点缀
def addition(n):
    for _ in range(n):
        x = random.randint(-180, 180)
        y = random.randint(0, 300)
        t1.penup()
        t2.penup()
        t1.goto(x, y)
        t2.goto(x, -y)
        t1.pendown()
        t2.pendown()
        t1.dot(6, '#f44a55')
        t2.dot(6, 'white')
        #leaf(2, '#f44a55', t1)
        #leaf(2, 'white', t2)

# 小恐龙
ls = [
'***********########*',
'**********##########',
'**********##*#######',
'**********##########',
'**********##########', 
'**********#####*****', 
'**********########**',
'#********#####******',
'#*******######******',
'##*****#########****',
'###***########*#****',
'##############******',
'##############******',
'*############*******',
'**##########********',
'***########*********',
'****######**********',
'****###*##**********',
'****##***#**********',
'****#****#**********',
'****##***##*********']

def draw_by_str(ls, size, color, t, flag):
    for i in ls:
        x = t.xcor()
        y = t.ycor()
        for j in i:
            if j == '#':
                square(size, color, t)
            t.penup()
            t.fd(size)
            t.pendown()
        t.penup()
        if(flag):
            t.goto(x, y - size)
        else:
            t.goto(x, y + size)

turtle.setworldcoordinates(-200, -300, 200, 300)
turtle.tracer(0)
#ang = 30
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.pencolor('#f44a55')

# 下侧填充
t1.fillcolor('#f44a55')
t1.begin_fill()
t1.fd(200)
t1.rt(90)
t1.fd(300)
t1.rt(90)
t1.fd(400)
t1.rt(90)
t1.fd(300)
t1.rt(90)
t1.fd(200)
t1.end_fill()

t2.pencolor('white')
t1.left(90)
t2.right(90)
'''
t.penup()
t.backward(45)
t.pendown()
'''
t1.pensize(20)
t2.pensize(20)
tree(60, t1)
tree(60, t2)

addition(200)

# 画小恐龙
t = turtle.Turtle()
t.penup()
t.fd(20)
t.lt(90)
t.fd(21*2)
t.rt(90)
t.pencolor('#f44a55')
draw_by_str(ls, 2, '#f44a55', t, True)
tt = turtle.Turtle()
tt.rt(180)
tt.penup()
tt.fd(20)
tt.lt(90)
tt.fd(21*2)
tt.rt(90)
tt.pencolor('white')
draw_by_str(ls, 2, 'white', tt, False)

t.hideturtle()
tt.hideturtle()
t1.hideturtle()
t2.hideturtle()
turtle.update()
turtle.done()
