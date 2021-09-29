# Internship Portal Web App
# __init__.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan

For now just store API in the __init__.py file, this will change later.
"""


# Flask Imports:
from flask import Flask
from flask_cors import CORS

# Imports for database ORM:
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Creates Flask app  with some configurations:
app = Flask(__name__,
            static_folder='../static',
            template_folder='../templates')


# Creates app:
def create_app():
    # Initial configurations:
    CORS(app)
    app.config['SECRET_KEY'] = ''
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://justinventura:justinventura@localhost:5432/internship_portal'

    # Wrap SQLAlchemy ORM to the app for database.
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    # Blueprint for views routes in the app:
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    # Blueprint for auth routes in the app:
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Return the app to be run in main.py:
    return app
