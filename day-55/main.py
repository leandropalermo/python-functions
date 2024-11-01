from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper(*args, **kwargs):
        message = function()
        return f"<b>{message}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper(*args, **kwargs):
        message = function()
        return f"<em>{message}</em>"
    return wrapper


def make_underlined(function):
    def wrapper(*args, **kwargs):
        message = function()
        return f"<u>{message}</u>"
    return wrapper


##http://127.0.0.1:5000/username/leandro
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return f"Bye"

@app.route("/username/<name>")
def hello_world(name):
    return f"Hello {name}"


# http://127.0.0.1:5000/username/leandro/something
@app.route("/username/<path:name>")
def hello_world_full_path(name):
    return f"Hello {name}'"


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
