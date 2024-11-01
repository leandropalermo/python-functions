import time
import turtle as t
from paddle import Paddle
from ball import Ball
from score import Score

score = Score()
screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_side_paddle = Paddle((350, 0))
left_side_paddle = Paddle((-350, 0))
ball = Ball((0, 0))

screen.listen()
screen.onkey(right_side_paddle.go_up, "Up")
screen.onkey(left_side_paddle.go_up, "w")
screen.onkey(right_side_paddle.go_down, "Down")
screen.onkey(left_side_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    if ball.distance(right_side_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(left_side_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
