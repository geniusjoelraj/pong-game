from turtle import *
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
screen.tracer(0)
screen.setup(width=1300, height=680)

paddle_left = Paddle((-600, 0))
paddle_right = Paddle((600, 0))

ball = Ball((0,0))
line_1 = Ball((0, 360))
line_2 = Ball((0, 320))
line_3 = Ball((0, 280))
line_4 = Ball((0, 240))
line_5 = Ball((0, 200))
line_6 = Ball((0, 160))
line_7 = Ball((0, 120))
line_8 = Ball((0, 80))
line_9 = Ball((0, 40))
line_10 = Ball((0, 0))
line_11 = Ball((0, -40))
line_12 = Ball((0, -80))
line_13 = Ball((0, -120))
line_14 = Ball((0, -160))
line_15 = Ball((0, -200))
line_16 = Ball((0, -240))
line_17 = Ball((0, -280))
line_18 = Ball((0, -320))
line_19 = Ball((0, -360))

scoreboard_p1 = Scoreboard((-100, 200))
scoreboard_p2 = Scoreboard((100, 200))

game_on = True

screen.listen()
screen.onkey(paddle_left.up, 'w')
screen.onkey(paddle_left.down, 's')
screen.onkey(paddle_right.up, 'Up')
screen.onkey(paddle_right.down, 'Down')
screen.update()
time.sleep(2)

while game_on:
    screen.update()
    if ball.ycor() > 360 or ball.ycor() < -360:
        ball.bounce()
    if ball.distance(paddle_right) <= 50 and ball.xcor() > 570 or ball.distance(paddle_left) <= 50 and ball.xcor() < -570:
        ball.deflect()
    if ball.xcor() > 700:
        scoreboard_p1.update_score()
        time.sleep(2)
        ball.respawn()
    elif ball.xcor() < -700:
        scoreboard_p2.update_score()
        time.sleep(2)
        ball.respawn()

    ball.move()

    





screen.mainloop()