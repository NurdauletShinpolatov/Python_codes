import turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.goto(-300, 0)
pen.goto(300, 0)
pen.home()
pen.goto(0, 300)
pen.goto(0, -300)
pen.home()
x = -300
y = 0
aaa, bbb = 10, -300
for i in range(120):
    
    x, y = bbb, 0
    pen.goto(x, y)
    if i > 59:
        bbb -= 10
    else:
        bbb += 10

    x, y = 0, aaa
    pen.goto(x, y)
    if i > 29 and i < 89:
        aaa -= 10
    if i < 28 or i > 89:
        aaa += 10



























    
