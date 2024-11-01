from turtle import Turtle


class TurtleObject(Turtle):

    def __init__(self):
        super().__init__()
        self.width = 50
        self.height = 50
        self.setheading(90)
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.reset_position()

    def go_up(self):
        new_y = self.ycor()
        if self.ycor() < 300:
            new_y += 20

        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(0, -280)
