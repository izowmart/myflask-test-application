from flask import render_template, Blueprint, request,flash, redirect, url_for
from flask_login import login_required, current_user

from project.home.forms import MessageForm
from project import db
from project.models import BlogPost

# config

home_blueprint = Blueprint('home', __name__, template_folder='templates')


# routes
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    error = None
    form = MessageForm(request.form)
    if form.validate():
        new_message = BlogPost(form.title.data, form.description.data, current_user.id)
        db.session.add(new_message)
        db.session.commit()
        flash('New entry was successfully posted. Thanks')
        return redirect(url_for('home.home'))
    else:
        posts = BlogPost.query.all()
        return render_template('index.html', posts=posts, form=form, error=error)


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')
