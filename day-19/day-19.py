import turtle as t

timmy = t.Turtle()
screen = t.Screen()

def move_forwards():
    timmy.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()