from flask import Blueprint, render_template
from flask_login import login_required, current_user
from Project.__init__ import db
#When possible, erase this comment. Its like an easter egg
main = Blueprint('main', __name__)

@main.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('home.html', name=current_user.name)
    else:
        return render_template('login.html')

@main.route('/home')
@login_required
def home():
    if current_user.email!='pedro9livares@gmail.com':
        return render_template('home.html', name=current_user.name)







