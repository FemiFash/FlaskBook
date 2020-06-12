from flask import Flask

from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app) 

from users.views import user_app  # registering blueprint app in central application.py file 
app.register_blueprint(user_app) # ..... for app to be used in any other module.
