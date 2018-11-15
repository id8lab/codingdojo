from flask import render_template
from app import app
from app.forms import LoginForm



@app.route('/')
@app.route("/index")
def home():
    return render_template('index.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup/', methods=["GET","POST"])
def signup():
    form = LoginForm()
    return render_template('signup.html', title='Sign In', form=form)
