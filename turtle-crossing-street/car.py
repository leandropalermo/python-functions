import random
from turtle import Turtle
from typing import List

COLORS = ["red", "yellow", "blue", "green", "orange", "purple"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.all_objects: List[Turtle] = []
        self.velocity = 0.1

    def increase_velocity(self):
        self.velocity *= 0.9

    def create_object(self):
        random_chance = random.randint(1, 6)
        if random_chance == 2:
            obj = Turtle()
            obj.shape("square")
            obj.shapesize(stretch_wid=1, stretch_len=2)
            obj.x_move = 30
            obj.y_position = random.randint(-250, 250)
            obj.penup()
            obj.color(random.choice(COLORS))
            obj.goto((300, obj.y_position))
            self.all_objects.append(obj)

    def move_objects(self):
        for obj in self.all_objects:
            obj.backward(5)
