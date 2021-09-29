# Internship Portal Web App
# __init__.py for API


"""
Clients: Dr. Joseph Anderson, Dr. Giulia Franchi
Team: Blaine Mason, Jacob Duncan, Justin Ventura, Margaret Finnegan

For now just store API in the __init__.py file, this will change later.
"""


# Flask Imports:
from flask import Flask, render_template, request
from flask_cors import CORS


# Creates Flask app  with some configurations:
app = Flask(__name__,
            static_folder='../static',
            template_folder='../templates')


# Creates app:
def create_app():
    # Initial configurations:
    CORS(app)
    app.config['SECRET_KEY'] = ''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/internship_portal'

    # Blueprint for views routes in the app:
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    # Blueprint for auth routes in the app:
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Return the app to be run in main.py:
    return app
