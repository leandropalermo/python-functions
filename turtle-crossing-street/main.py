import random
import time
from turtle import Turtle, Screen
from typing import List

from turtle_object import TurtleObject
from car import Car
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Street")
screen.tracer(0)

turtle = TurtleObject()
score = Score()
car = Car()


screen.listen()
screen.onkey(turtle.go_up, "Up")

# object = Object(-200, 280)
# object.x_move = 1
#
# object2 = Object(-50, -280)
# object2.x_move = 1
#
# object3 = Object(80, 280)
# object3.x_move = 1.2
#
# object4 = Object(170, -280)
# object4.x_move = 1.2
#
# object5 = Object(250, 280)
# object5.x_move = 1.5

game_is_on = True
while game_is_on:
    time.sleep(car.velocity)
    car.create_object()
    car.move_objects()
    screen.update()
    for c in car.all_objects:
        if turtle.distance(c) < 20:
            game_is_on = False
            score.lost_message()

    if turtle.ycor() >= 300:
        turtle.reset_position()
        car.increase_velocity()
        score.increase_level()
        score.update_level()


screen.exitonclick()
