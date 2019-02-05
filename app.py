from flask import Flask, redirect, url_for, request, render_template, session, flash
from functools import wraps
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "my precious"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create the sqlalchemy object
db = SQLAlchemy(app)
# model import done here and not at the top to cater for the sqlalchemy instance that is usefull at the model
from models import *


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))

    return wrap


@app.route('/')
@login_required
def home():

    # return "hello, world # return a string"
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render template inside the template folder


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'password':
            error = 'Invalid credentials.Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))


if __name__ == '__main__':
    app.run(debug=True)
