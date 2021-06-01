from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
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
        flash('Task added to database')
        return redirect(url_for("homepage"))
    return render_template("add.html", form=form)

@app.route('/edit<int:task_id>', methods=["POST", "GET"])
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()

    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            db.session.commit()
            flash('The task has beeen updated')
            return redirect(url_for("homepage"))
        form.title.data = task.title
        return render_template("edit.html", form=form, task_id=task_id)
    else:
        flash('The task was not found')
        return redirect(url_for("homepage"))