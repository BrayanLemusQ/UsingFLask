from app import app, db
from flask import render_template, redirect, url_for
from models import Task
import forms


@app.route('/')
@app.route('/index')
def homepage():
    tasks = Task.query.all()
    return render_template("index.html", tasks = tasks)

@app.route('/goodbye')
def goodbyepage():
    return render_template("goodbye.html", name="Brayan Lemus")

@app.route('/add', methods=["POST", "GET"])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        task = Task(title=form.title.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("homepage"))
    return render_template("add.html", form=form)