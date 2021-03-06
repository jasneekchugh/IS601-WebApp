from flask import current_app as app
from flask import render_template


@app.route("/")
def home():

    nav = [
        {"name": "Home", "url": "https://example.com/1"},
        {"name": "About", "url": "https://example.com/2"},
        {"name": "Pics", "url": "https://example.com/3"},
    ]
    return render_template(
        "home.html",
        nav=nav,
        title="Demo of Jinja Template in Flask by Jasneek Chugh",
        description=" Jinja is a templating system that empowers us to do things like share snippets between pages, or render pages conditionally based on context.",
    )