from turtle import Turtle
from typing import List

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_RIGHT_DIRECTION = 0
MOVE_LEFT_DIRECTION = 180
MOVE_UP_DIRECTION = 90
MOVE_DOWN_DIRECTION = 270


class Snake:

    def __init__(self):
        self.turtles: List[Turtle] = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_extend(position)

    def add_extend(self, position):
        t = Turtle("square")
        t.penup()
        t.goto(position)
        t.color("white")
        self.turtles.append(t)

    def extend(self):
        self.add_extend(self.turtles[-1].position())

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[i - 1].xcor()
            new_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != MOVE_DOWN_DIRECTION:
            self.head.setheading(MOVE_UP_DIRECTION)

    def down(self):
        if self.head.heading() != MOVE_UP_DIRECTION:
            self.head.setheading(MOVE_DOWN_DIRECTION)

    def left(self):
        if self.head.heading() != MOVE_RIGHT_DIRECTION:
            self.head.setheading(MOVE_LEFT_DIRECTION)

    def right(self):
        if self.head.heading() != MOVE_LEFT_DIRECTION:
            self.head.setheading(MOVE_RIGHT_DIRECTION)

    def reset(self):
        for turtle in self.turtles:
            turtle.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]
