import requests
from flask import Flask, render_template

BLOG_URL = "https://api.npoint.io/docs/c790b4d5cab58020d391"

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url=BLOG_URL)
    response.raise_for_status()
    print(response.text)
    data_json = response.json()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
