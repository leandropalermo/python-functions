from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['POST'])
def login():
    print(request.form['name'])
    print(request.form['password'])
    return ""


if __name__ == "__main__":
    app.run(debug=True)
