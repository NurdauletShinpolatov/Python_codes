# can be played, but a bit uncomfortable
# instead of clicking again, shoud drag
import turtle
import math
turtle.delay(0)
board = turtle.Turtle()
board.color('black', 'white')
board.speed(0)
board.pensize(3)
board.up()
board.goto(-300, 300)
color = 'white'
board.down()
for i in range(8):
    for i in range(8):
        board.color('black', color)
        board.begin_fill()
        for i in range(4):
            board.fd(75)
            board.rt(90)
        board.end_fill()
        board.fd(75)
        if color == 'grey':
            color = 'white'
        elif color == 'white':
            color = 'grey'
    if color == 'grey':
        color = 'white'
    elif color == 'white':
        color = 'grey'
    board.rt(90)
    board.fd(75)
    board.rt(90)
    board.fd(600)
    board.rt(180)
#=================================================
# C O R D I N A T E S
a1 = (-262.50,-262.50)
c1 = (-112.50,-262.50)
e1 = (37.50,-262.50)
g1 = (187.50,-262.50)

b2 = (-187.50,-187.50)
d2 = (-37.50,-187.50)
f2 = (112.50,-187.50)
h2 = (262.50,-187.50)

a3 = (-262.50,-112.50)
c3 = (-112.50,-112.50)
e3 = (37.50,-112.50)
g3 = (187.50,-112.50)

b4 = (-187.50,-37.50)
d4 = (-37.50,-37.50)
f4 = (112.50,-37.50)
h4 = (262.50,-37.50)

a5 = (-262.50,37.50)
c5 = (-112.50,37.50)
e5 = (37.50,37.50)
g5 = (187.50,37.50)

b6 = (-187.50,112.50)
d6 = (-37.50,112.50)
f6 = (112.50,112.50)
h6 = (262.50,112.50)

a7 = (-262.50,187.50)
c7 = (-112.50,187.50)
e7 = (37.50,187.50)
g7 = (187.50,187.50)

b8 = (-187.50,262.50)
d8 = (-37.50,262.50)
f8 = (112.50,262.50)
h8 = (262.50,262.50)
# END  C O R D I N A T E S
#============================================
blue1 = turtle.Turtle()  # creating blue turtles
blue2 = turtle.Turtle()
blue3 = turtle.Turtle()
blue4 = turtle.Turtle()
blue5 = turtle.Turtle()
blue6 = turtle.Turtle()
blue7 = turtle.Turtle()
blue8 = turtle.Turtle()
blue9 = turtle.Turtle()
blue10 = turtle.Turtle()
blue11 = turtle.Turtle()
blue12 = turtle.Turtle()

red1 = turtle.Turtle()  # creating red turtles
red2 = turtle.Turtle()
red3 = turtle.Turtle()
red4 = turtle.Turtle()
red5 = turtle.Turtle()
red6 = turtle.Turtle()
red7 = turtle.Turtle()
red8 = turtle.Turtle()
red9 = turtle.Turtle()
red10 = turtle.Turtle()
red11 = turtle.Turtle()
red12 = turtle.Turtle()

blue1.up()  # up() blue
blue2.up()
blue3.up()
blue4.up()
blue5.up()
blue6.up()
blue7.up()
blue8.up()
blue9.up()
blue10.up()
blue11.up()
blue12.up()

red1.up()  # up() red
red2.up()
red3.up()
red4.up()
red5.up()
red6.up()
red7.up()
red8.up()
red9.up()
red10.up()
red11.up()
red12.up()


blue1.shape('circle')  # giving circle shape to blue
blue2.shape('circle')
blue3.shape('circle')
blue4.shape('circle')
blue5.shape('circle')
blue6.shape('circle')
blue7.shape('circle')
blue8.shape('circle')
blue9.shape('circle')
blue10.shape('circle')
blue11.shape('circle')
blue12.shape('circle')

red1.shape('circle')  # giving circle shape to red
red2.shape('circle')
red3.shape('circle')
red4.shape('circle')
red5.shape('circle')
red6.shape('circle')
red7.shape('circle')
red8.shape('circle')
red9.shape('circle')
red10.shape('circle')
red11.shape('circle')
red12.shape('circle')

blue1.color('blue')   # giving blue color
blue2.color('blue')
blue3.color('blue')
blue4.color('blue')
blue5.color('blue')
blue6.color('blue')
blue7.color('blue')
blue8.color('blue')
blue9.color('blue')
blue10.color('blue')
blue11.color('blue')
blue12.color('blue')

red1.color('red')   # giving red color
red2.color('red')
red3.color('red')
red4.color('red')
red5.color('red')
red6.color('red')
red7.color('red')
red8.color('red')
red9.color('red')
red10.color('red')
red11.color('red')
red12.color('red')

red1.shapesize(3)   # increasing the shapesize of red
red2.shapesize(3)
red3.shapesize(3)
red4.shapesize(3)
red5.shapesize(3)
red6.shapesize(3)
red7.shapesize(3)
red8.shapesize(3)
red9.shapesize(3)
red10.shapesize(3)
red11.shapesize(3)
red12.shapesize(3)

blue1.shapesize(3)   # increasing the shapesize of blue
blue2.shapesize(3)   #
blue3.shapesize(3)   #
blue4.shapesize(3)   #
blue5.shapesize(3)   #
blue6.shapesize(3)   #
blue7.shapesize(3)   #
blue8.shapesize(3)   #
blue9.shapesize(3)   #
blue10.shapesize(3)  #
blue11.shapesize(3)  #
blue12.shapesize(3)  #

red1.goto(a1)   # putting the red on their places
red2.goto(c1)   #
red3.goto(e1)   #
red4.goto(g1)   #
red5.goto(b2)   #
red6.goto(d2)   #
red7.goto(f2)   #
red8.goto(h2)   #
red9.goto(a3)   #
red10.goto(c3)  #
red11.goto(e3)  #
red12.goto(g3)  #

blue1.goto(h8)    # putting the blue on their places
blue2.goto(f8)    #
blue3.goto(d8)    #
blue4.goto(b8)    #
blue5.goto(g7)    #
blue6.goto(e7)    #
blue7.goto(c7)    #
blue8.goto(a7)    #
blue9.goto(h6)    #
blue10.goto(f6)   #
blue11.goto(d6)   #
blue12.goto(b6)   #

taken_red = 0
taken_blue = 0
count = 0
red_taslar = [red1, red2, red3, red4, red5, red6, red7, red8, red9, red10, red11, red12]
blue_taslar = [blue1, blue2, blue3, blue4, blue5, blue6, blue7, blue8, blue9, blue10, blue11, blue12]
taken = False
def click(x, y):
    global taken
    global taken_red
    global taken_blue
    global count
    
    for queue in ('red', 'blue'):
        count = 0
        if queue == 'red':
            for tas in red_taslar:
                count += 1
                clx_tas = math.fabs(x - tas.xcor())
                if clx_tas < 61:
                    cly_tas = math.fabs(y - tas.ycor())
                    if cly_tas <61:
                        taken_red = count
                        taken_blue = 0
                        break
        else:
            for tas in blue_taslar:
                count += 1
                clx_tas = math.fabs(x - tas.xcor())
                if clx_tas < 61:
                    cly_tas = math.fabs(y - tas.ycor())
                    if cly_tas <61:
                        taken_blue = count
                        taken_red = 0
                        break
    if taken_red > 0 and taken == False:
        red_taslar[taken_red - 1].color('orange')
        taken = True
    elif taken_red > 0 and taken == True:
        red_taslar[taken_red - 1].goto(x, y)
        red_taslar[taken_red - 1].color('red')
        taken = False
    elif taken_blue > 0 and taken == False:
        blue_taslar[taken_blue - 1].color('green')
        taken = True
    elif taken_blue > 0 and taken == True:
        blue_taslar[taken_blue - 1].goto(x, y)
        blue_taslar[taken_blue - 1].color('blue')
        taken = False
    
    

    
turtle.listen()
turtle.onscreenclick(click, btn=1)








