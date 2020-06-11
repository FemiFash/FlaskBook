from flask import Flask


def create_app():
	app = Flask(__name__)
	app.config.from_pyfile('settings.py')
	# app.config.from_object('settings')
	
	from user.views import user_app  # registering blueprint app in central application.py file
	app.register_blueprint(user_app) # ..... for app to be used in any other module
	
	return app
