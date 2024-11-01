import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


games_on = True
while games_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreBoard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreBoard.reset()
        snake.reset()

    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 5:
            scoreBoard.reset()
            snake.reset()

screen.exitonclick()
