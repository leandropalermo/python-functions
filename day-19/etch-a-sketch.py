import turtle as t

timmy = t.Turtle()
screen = t.Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_left():
    heading = timmy.heading()
    timmy.setheading(heading + 10)

def turn_right():
    heading = timmy.heading()
    timmy.setheading(heading - 10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()