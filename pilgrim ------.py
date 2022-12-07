import turtle
player = turtle.Turtle()
player.hideturtle()
player.speed(0)
turtle.delay(0)


def square(cordinate):
    turtle.up()
    turtle.goto(cordinate)
    turtle.down()
    for index in range(4):
        turtle.fd(100)
        turtle.rt(90)


cordinates = [(-200, 200), (-100, 200), (0, 200), (100, 200),
              (-200, 100), (-100, 100), (0, 100), (100, 100),
              (-200, 0), (-100, 0), (0, 0), (100, 0),
              (-200, -100), (-100, -100), (0, -100), (100, -100)]


def draw():
    for cordinate in cordinates:
        square(cordinate)
player.up()
draw()
player.up()
player.goto(0, 200)
v = 100
fee = 4
player.pensize(4)
player.color("red")
player.down()
turtle.listen()
player.shape("circle")
player.shapesize(1.5)
player.showturtle()
turtle.hideturtle()

pen = turtle.Turtle()
pen.hideturtle()
def writefee(fee):
    pen.goto(0, 230)
    pen.clear()
    pen.write(f"fee is {fee}", move=False, align="left", font=("Arial", 24, "normal"))
def up():
    global fee
    fee /= 2
    player.goto(player.xcor(), player.ycor()+v)
    writefee(fee)
def down():
    global fee
    fee *= 2
    player.goto(player.xcor(), player.ycor()-v)
    writefee(fee)
def right():
    global fee
    fee += 2
    player.goto(player.xcor()+v, player.ycor())
    writefee(fee)
def left():
    global fee
    fee -= 2
    player.goto(player.xcor()-v, player.ycor())
    writefee(fee)
def r():
    global fee
    turtle.up()
    turtle.clear()
    draw()
    player.clear()
    player.up()
    player.goto(-200, 200)
    player.down()
    player.goto(0, 200)
    fee = 4
    pen.write(f"fee is {fee}", move=False, align="left", font=("Arial", 24, "normal"))
turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(right, 'Right')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(r, 'r')
