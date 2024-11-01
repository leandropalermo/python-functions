import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

us_states_df = pandas.read_csv("us_states_data.csv")
us_states_list = us_states_df.state.to_list()

guess_state = []

while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in us_states_list if state not in guess_state]
        missing_states_df = pandas.DataFrame(missing_states)
        missing_states_df.to_csv("states_to_learn.csv")
        break

    if answer_state in us_states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = us_states_df[us_states_df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guess_state.append(answer_state)




def get_mouse_click_coord(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coord)
turtle.mainloop()

