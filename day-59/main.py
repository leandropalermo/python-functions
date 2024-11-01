from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/")
@app.route("/index.html")
def index():
    header_image = 'home-bg.jpg'
    header_div_class = 'site-heading'
    header_title = 'Clean Blog'
    header_subtitle = 'A Blog Theme by Start Bootstrap'
    return render_template("index.html",
                           header_image=header_image,
                           header_div_class=header_div_class,
                           header_subtitle=header_subtitle,
                           header_title=header_title)


@app.route("/contact")
def contact():
    header_image = 'contact-bg.jpg'
    header_div_class = 'page-heading'
    header_title = 'Contact Me'
    header_subtitle = 'Have questions? I have answers.'
    return render_template("contact.html",
                           header_image=header_image,
                           header_div_class=header_div_class,
                           header_title=header_title,
                           header_subtitle=header_subtitle)


@app.route("/about")
def about():
    header_image = 'about-bg.jpg'
    header_div_class = 'page-heading'
    header_title = 'About Me'
    header_subtitle = 'This is what I do.'
    return render_template("about.html",
                           header_image=header_image,
                           header_div_class=header_div_class,
                           header_title=header_title,
                           header_subtitle=header_subtitle)


@app.route("/post")
def post():
    header_image = 'post-bg.jpg'
    header_div_class = 'page-heading'
    header_title = 'Man must explore, and this is exploration at its greatest'
    header_subtitle = 'Problems look mighty small from 150 miles up'
    return render_template("post.html",
                           header_image=header_image,
                           header_div_class=header_div_class,
                           header_title=header_title,
                           header_subtitle=header_subtitle)


@app.route("/receive_data", methods=['POST'])
def receive_data():
    print("passing here")
    print(request.form['name'])
    print(request.form['email'])
    return "<h1>Successfully sent your message</h1>"

if __name__ == '__main__':
    app.run(debug=True)