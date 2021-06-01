from app import app
from flask import render_template
import forms


@app.route('/')
@app.route('/index')
def homepage():
    return render_template("index.html", name="Brayan Lemus")

@app.route('/goodbye')
def goodbyepage():
    return render_template("goodbye.html", name="Brayan Lemus")

@app.route('/add', methods=["POST", "GET"])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        return render_template("add.html", form=form, title=form.title.data)
    return render_template("add.html", form=form)