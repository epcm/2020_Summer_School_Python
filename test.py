import pgzrun

RED = 200, 0, 0
BOX = Rect((100, 20), (200, 100))

ls = []

def draw():
    screen.draw.rect(BOX, RED)

pgzrun.go()
for _ in range(10):
    t.setheading(random.randint(0, 360))
    temp = math.cos(math.radians(t.heading() + 5)) / 8 + 0.25
    t.pencolor(temp*1.6, temp*1.2, temp*1.4)
    t.fd(100)
turtle.done()

#colors = ['#f44a55', 'white', '#ffcccc']
print('assd')
