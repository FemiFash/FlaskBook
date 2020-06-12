from flask import Blueprint

user_app = Blueprint('user_app', __name__)   # Anything named *_app is a Blueprint app

@user_app.route('/')
@user_app.route('/index/')
def index():
	return "Index Page"

@user_app.route('/login')
def login():
	return "User login"


