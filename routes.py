from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def homepage():
    return render_template("index.html", name="Brayan Lemus")

@app.route('/goodbye')
def goodbyepage():
    return render_template("goodbye.html", name="Brayan Lemus")