# // Analoc clock with turtle
from datetime import datetime
import time
import turtle

# // Initialising a turtle
turtle.delay(0)
pen = turtle.Turtle()
pen.speed(0)
pen.shape('circle')
pen.up()
pen.goto(0, -300)
pen.down()


# // Drawing the clock
for i in range(60):
    pen.circle(300, 6)

    # // main 4 lines of 12,3,6,9
    if i==14 or i==29 or i==44 or i==59: 
        pen.pensize(3)
        pen.color('red')
        pen.lt(90)
        pen.fd(60)
        pen.bk(60)
        pen.rt(90)
        pen.pensize(1)
        pen.color('black')

    # // every 5 min lines
    elif i==4 or i==9 or i==19 or i==24 or i==34 or i==39 or i==49 or i==54:
        pen.pensize(3)
        pen.color('red')
        pen.lt(90)
        pen.fd(30)
        pen.bk(30)
        pen.rt(90)
        pen.pensize(1)
        pen.color('black')

    # // every sec/min lines
    else:
        pen.pensize(1)
        pen.color('black')
        pen.lt(90)
        pen.fd(15)
        pen.bk(15)
        pen.rt(90)


# // Initialising h, m, s turtles
hour = turtle.Turtle()      #
minute = turtle.Turtle()    # // getting turtles
second = turtle.Turtle()    #

hour.shape('arrow')     #
minute.shape('arrow')   # // shape
second.shape('arrow')   #

hour.color('black')     #
minute.color('blue')    # // colour
second.color('red')     #

hour.shapesize(0.5, 13)     #
second.shapesize(0.3, 20)   # // size of shape
minute.shapesize(0.5, 18)   #

hour.lt(90)     #
minute.lt(90)   # // giving initial position at 12:00
second.lt(90)   #


# // Getting current time and show time
now = datetime.now()
hh = int(now.strftime("%H"))
mm = int(now.strftime("%M"))
ss = int(now.strftime("%S"))

hour.rt(hh*30 + mm*0.5 + ss*0.5/60)
minute.rt(mm*6)
second.rt(ss*6)

pen.up()
pen.home()

# Moving 
while True:
    time.sleep(1)
    second.rt(6)
    if second.heading() == 90:
        minute.rt(6)
        hour.rt(0.5)
