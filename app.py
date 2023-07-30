from flask import Flask

app = Flask('flask')

@app.route("/")
def hello():
    return "Hello, World!"