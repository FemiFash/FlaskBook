from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Configure app & database
app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app) 

# migrations
migrate = Migrate(app, db)

# registering blueprint app in central application.py  
# file for app to be used in any other module.
from users.views import user_app  
app.register_blueprint(user_app)
