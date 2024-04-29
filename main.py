from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce
        ball.bounce()

    #detect colision with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.change_direction()
        # print("ball hit paddle")

    # detect when paddle misses
    if ball.xcor() > 380:
        ball.ball_restart()
        score.l_point()

    if ball.xcor() < -380:
        ball.ball_restart()
        score.r_point()



screen.exitonclick()