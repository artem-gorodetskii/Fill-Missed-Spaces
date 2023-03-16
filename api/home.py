import flask
from flask import render_template


routes = flask.Blueprint('home', __name__)


@routes.route('/')
def home():
    r"""Renders the homepage."""
    return render_template('home.html')
