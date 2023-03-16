import flask
from flask import jsonify


routes = flask.Blueprint('errorhandler', __name__)


@routes.app_errorhandler(405)
def method_not_allowed(error):
    r"""If a request has the wrong method to our API."""
    return jsonify(message = "Method Not Allowed"), 405
