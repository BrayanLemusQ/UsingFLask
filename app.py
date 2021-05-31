from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def homepage():
    return render_template("index.html")

@app.route('/goodbye')
def goodbyepage():
    return "<h1>Goodbye!<h1>"

if __name__=='main':
    app.run(debug=True)