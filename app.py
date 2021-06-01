from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SECRET_KEY"] = "PASSWORD"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'

db = SQLAlchemy(app)

from routes import *

if __name__=='main':
    app.run(debug=True)