from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config['SECRET_KEY']


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")