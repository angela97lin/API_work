# Justin Strauss and Angela Lin
# Software Development Period 7
# API Project

from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
@app.route('/index', methods=["POST","GET"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
