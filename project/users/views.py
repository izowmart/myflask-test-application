from flask import flash, redirect, render_template, request, url_for, Blueprint, session
from flask_login import login_user, login_required, logout_user

from .forms import LoginForm, RegisterForm
from project import db
from project.models import User, bcrypt


users_blueprint = Blueprint('users', __name__, template_folder='templates')


# routes
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter(User.name == request.form['username']).first()
        if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            flash('You were logged in. You gat it Booy!')
            return redirect(url_for('home.home'))
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out!')
    return redirect(url_for('home.welcome'))


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate():
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home.home'))
    return render_template('register.html', form=form)

