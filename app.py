from flask import Flask

app=Flask(__name__)

@app.route('/')
def homepage():
    return "Virtual Environment and Flask Running"

if __name__=='main':
    app.run(debug=True)