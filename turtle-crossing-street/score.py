from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
MESSAGE_POSITION = (-10, 150)
LEVEL_MESSAGE_POSITION = (-200, 250)

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(LEVEL_MESSAGE_POSITION)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1

    def lost_message(self):
        self.clear()
        self.goto(MESSAGE_POSITION)
        self.write(f"Game Over\nYou lose!", align=ALIGNMENT, font=FONT)

