# ping pong game 1/5

import turtle
import winsound
import time
wn = turtle.Screen()
wn.title('Pong by Nurdaulet')
wn.bgcolor('black')
wn.tracer(1)

#       B O R 
bor = turtle.Turtle()
bor.hideturtle()
bor.up()
bor.goto(-300,200)
bor.color('blue')
bor.pensize(5)
bor.shape('circle')
bor.down()
bor.speed(0)

for i in range(2):
    bor.fd(600)
    bor.rt(90)
    bor.color('red')
    bor.fd(400)
    bor.rt(90)
    bor.color('blue')

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.up()
paddle_a.goto(-250, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.up()
paddle_b.goto(250, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.up()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# Score
score_a = 0
score_b = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.up()
pen.hideturtle()
pen.goto(0, 220)
pen.write('Use s, w, UP and DOWN keys to play', align='center', font=('Courier', 24, 'normal'))
time.sleep(3)
pen.clear()
pen.write('Player A: {} Player B: {}'.format(score_a, score_b),score_b, align='center', font=('Courier', 24, 'normal'))


# function
def a_up():
    if paddle_a.ycor() < 140:
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)
def a_down():
    if paddle_a.ycor() > -140:
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)
def b_up():
    if paddle_b.ycor() < 140:
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)
def b_down():
    if paddle_b.ycor() > -140:
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(a_up, 'w')
wn.onkeypress(a_down, 's')
wn.onkeypress(b_up, 'Up')
wn.onkeypress(b_down, 'Down')

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1
        ##winsound.PlaySound('Click2-Sebastian-759472264.wav', winsound.SND_ASYNC)
        
    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.goto(0, 220)
        ##winsound.PlaySound('Bow_Fire_Arrow-Stephan_Schutze-2133929391.wav', winsound.SND_ASYNC)
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b),score_b, align='center', font=('Courier', 24, 'normal'))
        time.sleep(1)
    if ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.goto(0, 220)
        ##winsound.PlaySound('Bow_Fire_Arrow-Stephan_Schutze-2133929391.wav', winsound.SND_ASYNC)
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b),score_b, align='center', font=('Courier', 24, 'normal'))
        time.sleep(1)

    # Paddle and ball collision
    if (ball.xcor() > 240 and ball.xcor() < 250)and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(240)
        ##winsound.PlaySound('Click2-Sebastian-759472264.wav', winsound.SND_ASYNC)
        ball.dx *= -1
        
    if (ball.xcor() < -240 and ball.xcor() > -250)and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-240)
        ##winsound.PlaySound('Click2-Sebastian-759472264.wav', winsound.SND_ASYNC)
        ball.dx *= -1
