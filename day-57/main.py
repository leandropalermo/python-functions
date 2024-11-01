import random
import time
from datetime import date

import requests
from flask import Flask, render_template

AGIFY_URL = 'https://api.agify.io'
GENDERIZE_URL = 'https://api.genderize.io/'
BLOG_URL = "https://api.npoint.io/147751ff3516a344ae1e"
app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = date.today().year
    return render_template("index.html", random_number=random_number, year=year, name='Leandro')


@app.route("/guess/<string:name>")
def guess(name):
    agify_params = {
        "name": name
    }
    agify_response = requests.get(url=AGIFY_URL, params=agify_params)
    age = agify_response.json().get('age')

    genderize_params = {
        "name": name
    }
    genderize_response = requests.get(url=GENDERIZE_URL, params=genderize_params)
    gender = genderize_response.json().get('gender')

    return render_template("guess.html", name=name, gender=gender.title(), age=age)


@app.route("/blog/<num>")
def get_blog(num):
    response = requests.get(url=BLOG_URL)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)