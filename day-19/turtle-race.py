import random
import turtle as t

screen = t.Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet.",
                 "Which turtle will win the race? Enter a color: ")

colors = ["red", "yellow", "blue", "green", "orange", "purple"]
y_positions = [-60, -20, 20, 60, 100, 140]
is_race_on = False
all_turtles = []

for i in range(0, 6):
    turtle = t.Turtle("turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(-230, y_positions[i])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!" )
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()