#from application import app
from flask import Blueprint, render_template, redirect, url_for, flash
from users.forms import RegisterForm

user_app = Blueprint('user_app', __name__)   # Anything named *_app is a Blueprint app

@user_app.route('/')
@user_app.route('/index/')
def index():
	return "Index Page"

@user_app.route('/login')
def login():
	return "User login"

@user_app.route('/register', methods=('GET', 'POST'))
def register():
	form = RegisterForm()

	return render_template('users/register.html',form=form)
