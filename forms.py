from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AddTaskForm(FlaskForm):
    title = StringField("Title")
    submit =SubmitField("Submit")