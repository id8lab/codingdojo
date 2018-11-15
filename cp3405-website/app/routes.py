from flask import render_template
from app import app

@app.route('/')
@app.route("/index")
def home():
    return render_template('index.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')
