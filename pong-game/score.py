from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.update_score_board()

    def l_point(self):
        self.l_score += 1
        self.update_score_board()

    def r_point(self):
        self.r_score += 1
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

