from flask import Flask

app=Flask(__name__)
app.config["SECRET_KEY"] = "PASSWORD"
from routes import *

if __name__=='main':
    app.run(debug=True)