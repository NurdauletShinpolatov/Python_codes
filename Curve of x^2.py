import turtle
import math

window = turtle.Screen()
window.bgcolor('black')

cors = turtle.Turtle()
cors.shape('circle')
cors.shapesize(0.2)
cors.speed(0)
cors.color('white')
cors.goto(-300, 0)
for i in range(30):
    cors.clone()
    cors.fd(20)
    if i == 29:
        cors.shape('arrow')
        cors.shapesize(1)
    cors.clone()
cors.home()
cors.goto(0, 300)
cors.lt(90)
cors.clone()
cors.rt(180)
cors.shape('circle')
cors.shapesize(0.2)
for i in range(30):
    cors.fd(20)
    cors.clone()
cors.home()

graph = turtle.Turtle()
graph.hideturtle()
graph.color('red')
graph.up()
x = -80
times = 0
while graph.xcor() < 80:
    x_ed = x/20
    if times == 1:
        graph.down()
    y_ed = x_ed**2 # f u n k c i y a
    y = y_ed * 20
    graph.goto(x, y)
    x += 1
    times += 1





















