from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("pink")
screen.setup(width=800, height=600)
screen.title("Ping Pong motherfucker")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = Turtle
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < - 330:
        ball.bounce_x()
        print(ball.move_speed)

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        ball.bounce_x()


screen.exitonclick()
