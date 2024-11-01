import random

from flask import Flask

app = Flask(__name__)

number = random.randint(0, 9)

@app.route("/home")
def home():
    return "<H1 style='text-align: center'>Guess a number between 0 and 9.</H1> " \
           "<IMG style='display: block; margin-left: auto; margin-right: auto;' SRC='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/home/guess/<int:guess_number>")
def guess_a_number(guess_number):
    if guess_number > number:
        return "<H1 style='text-align: center; color: purple'>Too high, try again!.</H1> " \
               "<IMG style='display: block; margin-left: auto; margin-right: auto;' SRC='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif guess_number < number:
        return "<H1 style='text-align: center; color: red'>Too low, try again!.</H1> " \
               "<IMG style='display: block; margin-left: auto; margin-right: auto;' SRC='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<H1 style='text-align: center; color: green'>You found me!</H1> " \
        "<IMG style='display: block; margin-left: auto; margin-right: auto;' SRC='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"



if __name__ == '__main__':
    # app.run()
    app.run(debug=True)