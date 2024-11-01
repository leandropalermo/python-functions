from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_score()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()
        self.hideturtle()

    def read_score(self):
        with (open("data.txt")) as file:
            high_score = file.read()
            if high_score == "":
                high_score = 0
            self.high_score = high_score

    def save_score(self):
        with (open("data.txt", mode="w")) as file:
            print(f"saving {self.high_score}")
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            self.save_score()

        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

