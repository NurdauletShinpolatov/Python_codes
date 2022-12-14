import turtle
import random
import time
turtle.delay(0)
level = 0
count = 0
mistakes = 0
#// creating turtles as button
aaaa = turtle.Turtle()
bbbb = turtle.Turtle()
cccc = turtle.Turtle()
dddd = turtle.Turtle()
eeee = turtle.Turtle()
ffff = turtle.Turtle()
gggg = turtle.Turtle()
hhhh = turtle.Turtle()
iiii = turtle.Turtle()


#// turtle as one main button
button = turtle.Turtle()
button.up()
button.goto(0, 190)
button.shape('square')
button.shapesize(3, 16)
button.color('blue')

pen = turtle.Turtle()
pen.up()
pen.goto(0, -230)
pen.hideturtle()


#// coordinates of buttons
a = (-100, 100)
b = (0, 100)
c = (100, 100)
d = (-100, 0)   
e = (0, 0)
f = (100, 0)
g = (-100, -100)
h = (0, -100)
i = (100, -100)


#// lists 
coordinates = [a, b, c, d, e, f, g, h, i]
turtles = [aaaa, bbbb, cccc, dddd, eeee, ffff, gggg, hhhh, iiii]
challenge = []
following = []




#// making turtle like buttons
for index in range(9):
    turtles[index].shape('square')
    turtles[index].color('grey')
    turtles[index].up()
    turtles[index].goto(coordinates[index])
    turtles[index].shapesize(4)


#===========================================
#// FUNCTIONS

#// function that challenges
def challenging():
    global level
    level += 1
    button.color('white')
    following.clear()
    challenge.append(random.choice(turtles))
    time.sleep(0.75)
    for buttons in challenge:
        clicked(buttons)
        time.sleep(0.75)
    button.color('blue')

#// animation of clicked button
def clicked(button):
    pen.clear()
##    pen.write(arg, move=False, align="left", font=("Arial", 8, "normal"))
    pen.write(str(count)+" / "+str(level)+"\n"+str(mistakes)+" mistakes total", align="center", font=("Arial", 24, "normal"))
    for size in range(40, 32, -1):
        button.shapesize(size/10)
        time.sleep(0.01)
    for size in range(32, 40, 1):
        button.shapesize(size/10)
        time.sleep(0.01)


#// function that works when somewhere is clicked
def click(x, y):
    global count
    global mistakes
    if -150<x<150 and -150<y<150:
        count += 1
    if (x<-50 and x>-150) and (y>50 and y<150):     # 1
        following.append(aaaa)
        clicked(aaaa)
    elif (x<50 and x>-50) and (y>50 and y<150):     # 2
        following.append(bbbb)
        clicked(bbbb)
    elif (x<150 and x>50) and (y>50 and y<150):     # 3
        following.append(cccc)
        clicked(cccc)
    elif (x<-50 and x>-150) and (y>-50 and y<50):   # 4
        following.append(dddd)
        clicked(dddd)
    elif (x<50 and x>-50) and (y>-50 and y<50):     # 5
        following.append(eeee)
        clicked(eeee)
    elif (x<150 and x>50) and (y>-50 and y<50):     # 6
        following.append(ffff)
        clicked(ffff)
    elif (x<-50 and x>-150) and (y>-150 and y<-50): # 7
        following.append(gggg)
        clicked(gggg)
    elif (x<50 and x>-50) and (y>-150 and y<-50):   # 8
        following.append(hhhh)
        clicked(hhhh)
    elif (x<150 and x>50) and (y>-150 and y<-50):   # 9
        following.append(iiii)
        clicked(iiii)
    elif (x<160 and x>-160) and (y>160 and y<210):  # main bottom
        challenging()
    

    #// checking player move wether they are correct
    if following==challenge and len(challenge)!=0 and len(following)!=0:
        pen.color("green")
        pen.clear()
        pen.write(str(count)+" / "+str(level)+"\n"+str(mistakes)+" mistakes total", align="center", font=("Arial", 24, "normal"))
        count = 0
        pen.color("black")
        following.clear()
        button.color('green')
        time.sleep(1)
        button.color('blue')
    elif len(challenge)==len(following) and following!=challenge:
        mistakes += 1
        pen.color("red")
        pen.clear()
        pen.write(str(count)+" / "+str(level)+"\n"+str(mistakes)+" mistakes total", align="center", font=("Arial", 24, "normal"))
        count = 0
        pen.color("black")
        following.clear()
        button.color('red')
        time.sleep(1)
        button.color('blue')
        
turtle.onscreenclick(click, btn=1)

