from os import name
from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def homepage():
    return render_template("index.html", name="Brayan Lemus")

@app.route('/goodbye')
def goodbyepage():
    return render_template("goodbye.html", name="Brayan Lemus")

if __name__=='main':
    app.run(debug=True)