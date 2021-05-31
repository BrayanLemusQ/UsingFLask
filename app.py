from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def homepage():
    return "<h1>Bienvenidos!<h1>"

if __name__=='main':
    app.run(debug=True)